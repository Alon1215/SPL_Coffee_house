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
        if self.dbExist:
            os.remove('moncafe.db')
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

    def get_total_income(self, id):
        total = 0
        my_activities_value = self._conn.cursor().execute("""
                SELECT act.quantity prod.price FROM Activities act
                JOIN Products prod ON act.product_id = prod.id
                ORDER BY cow.name
                """).fetchall()
        for item in my_activities_value:
            total += item[0]



    def print_coffee_stands(self):
        print("Coffee stands")

        all = self._conn.cursor().execute("""
                SELECT * FROM Coffee_stands
                ORDER BY id
                """).fetchall()
        for line in all:
            print(line)

    def print_employees(self):
        print("Employees")
        all = self._conn.cursor().execute("""
                SELECT * FROM Suppliers
                ORDER BY id
                """).fetchall()
        for line in all:
            print(line)

    def print_suppliers(self):
        print("Suppliers")
        all = self._conn.cursor().execute("""
                SELECT * FROM Suppliers
                ORDER BY id
                """).fetchall()
        for line in all:
            print(line)

    def print_products(self):
        print("Products")
        all = self._conn.cursor().execute("""
                SELECT * FROM Products
                ORDER BY product_id
                """).fetchall()
        for line in all:
            print(line)

    def print_employees_report(self):
        print("Employees report")
        all = self._conn.cursor().execute("""
                                            SELECT emp.id emp.name, emp.salary, cf.location FROM Employees emp
                                            LEFT JOIN Coffee_stands cf ON cf.id = emp.coffee_stand
                                            ORDER BY cow.name
                                            """).fetchall()
        for item in list:
            int total = get_total_income(item[0])
            print("%s %s %s %s" % (item[1], item[2], item[3], total))

    def print_activities_report(self):
        print("Activities")
        all = self._conn.cursor().execute("""
                        SELECT * FROM Products
                        ORDER BY date
                        """).fetchall()
        for line in all:
            print(line)

    def print_activities_bottom(self):
        print("Activities")

    def print_all(self):
        self.print_activities_report()
        self.print_coffee_stands()
        self.print_employees()
        self.print_products()
        self.print_suppliers()
        self.print_activities_bottom()


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
