# The Repository
from DAOs import _CoffeeStands, _Employees, _Suppliers, _Activities, _Products
import sqlite3
import atexit
import os  # for remove # TODO: ALON 1320 remember to delete the line!


# The Repository

class _Repository:
    def __init__(self):

        # todo: change logic to check first if it exist, then create a fresh one
        self.dbExist = os.path.isfile('moncafe.db')
        self._conn = sqlite3.connect('moncafe.db')
        self.CoffeeStands = _CoffeeStands(self._conn)
        self.Employees = _Employees(self._conn)
        self.Suppliers = _Suppliers(self._conn)
        self.Activities = _Activities(self._conn)
        self.Products = _Products(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        if self.dbExist:
            self.fix_connect()
        self._conn.executescript("""
                CREATE TABLE Employees (id   INT   PRIMARY KEY,
                                       name TEXT  NOT NULL,
                                       salary REAL NOT NULL,
                                       coffee_stand INT, 
                                       
                                       FOREIGN KEY(coffee_stand)    REFERENCES Coffee_stand(id)
                );

                CREATE TABLE Suppliers (id  INT   PRIMARY KEY,
                                        name TEXT    NOT NULL,
                                        contact_information TEXT
                                        
                );

                CREATE TABLE Products (id      INT     PRIMARY KEY,
                                     description  TEXT     NOT NULL,
                                     price        REAL     NOT NULL,
                                     quantity INTEGER NOT NULL
                                     
                );
                
                CREATE TABLE Coffee_stands (id INT  PRIMARY KEY,                
                                            location TEXT NOT NULL,
                                            number_of_employees INTEGER
                                
                );                    
                CREATE TABLE Activities (product_id INT ,
                                        quantity INT NOT NULL,
                                        activator_id INT NOT NULL,
                                        date DATE NOT NULL,
                                        
                                        FOREIGN KEY(product_id)   REFERENCES Products(id)
                );
        """)

    def print_activities(self):
        print("Activities")

        all = self.Activities.find_all()
        for activity in all:
            print(activity)

    def get_total_income(self, employee_id):
        total = 0
        my_activities_value = self._conn.cursor().execute("""
                SELECT Activities.quantity, price FROM Activities 
                JOIN Products ON Activities.product_id = Products.id 
                WHERE activator_id=?
                """, [employee_id]).fetchall()
        for item in my_activities_value:
            total += (abs(item[0]) * item[1])
        return total

    def print_coffee_stands(self):
        print("Coffee stands")

        all = self.CoffeeStands.find_all()
        for stand in all:
            print(stand)

    def print_employees(self):
        print("Employees")
        all = self.Employees.find_all()
        for employee in all:
            print(employee)


    def print_suppliers(self):
        print("Suppliers")
        all = self.Suppliers.find_all()
        for supplier in all:
            print(supplier)


    def print_products(self):
        print("Products")
        all = self.Products.find_all()
        for product in all:
            print(product)

    def print_employees_report(self):
        print("Employees report")
        all = self._conn.cursor().execute("""
                                            SELECT Employees.id ,name, salary, location FROM Employees 
                                            JOIN Coffee_stands  ON  Coffee_stands.id = Employees.coffee_stand
                                            ORDER BY Employees.name

                                            """).fetchall()
        for item in all:
            total = self.get_total_income(item[0])
            print("%s %s %s %s" % (item[1], item[2], item[3], total))

    def print_activities_report(self):
        print("Activities")

        all = self._conn.cursor().execute("""SELECT date, description, Activities.quantity ,Employees.name,Suppliers.name FROM Activities
                               JOIN Products ON Activities.product_id = Products.id
                                LEFT JOIN Employees ON Activities.activator_id = Employees.id
                                LEFT JOIN Suppliers ON Activities.activator_id = Suppliers.id
                                ORDER BY Activities.date """).fetchall()

        for line in all:
            print(line)

    def print_all(self):
        self.print_db()
        self.print_employees_report()
        self.print_activities_report()

    def print_db(self):
        self.print_activities()
        self.print_coffee_stands()
        self.print_employees()
        self.print_products()
        self.print_suppliers()

    def fix_connect(self):
        self._delete_file()
        self.update_fields()

    def update_fields(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.CoffeeStands = _CoffeeStands(self._conn)
        self.Employees = _Employees(self._conn)
        self.Suppliers = _Suppliers(self._conn)
        self.Activities = _Activities(self._conn)
        self.Products = _Products(self._conn)

    def _delete_file(self):
        self._conn.commit()
        self._conn.close()
        os.remove('moncafe.db')


# the repository singleton
repo = _Repository()
atexit.register(repo._close)

