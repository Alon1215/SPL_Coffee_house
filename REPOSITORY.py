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
                
                CREATE TABLE Coffee_stands (product_id INTEGER  
                                            quantity INTEGER NOT NULL,
                                            activator_id INTEGER NOT NULL,
                                            date DATE NOT NULL,
                                    FOREIGN KEY(product_id)    REFERENCES Products(id)
                                    
                CREATE TABLE Activities (product_id INTEGER ,
                                        quantity INTEGER NOT NULL,
                                        activator_id INTEGER NOT NULL,
                                        date DATE NOT NULL,
                                        
                                        FOREIGN KEY(product_id)   REFERENCES Products(id)
                );
        """)

    # The method print_grades at the application logic (main) is inefficient because
    # it goes over all the students one by one in order to find the name of the student
    # Using join query matches between the student's grade and name.
    def get_grades_with_names(self):
        all = self._conn.cursor().execute("""
            SELECT students.name, grades.assignment_num, grades.grade
            FROM grades
            JOIN students ON grades.student_id = students.id
        """).fetchall()

        # Just for debaug - The difference between row and *row
        for row in all:
            print(row)
            print(*row)

        return [StudentGrade(*row) for row in all]

    def print_coffee_stands(self):
        print("Coffee stands")
        c = self._conn.cursor()
        all = c.execute(""" SELECT * FROM """)
        for line in all:
            print(line)



    def print_emoloyees(self):
        print("Employees")

    def print_suppliers(self):
        print("Suppliers")

    def print_products(self):
        print("Products")

    def print_activities_top(self):
        print("Activities")

    def print_activities_bottom(self):
        print("Activities")

    def print_tables(self):
        self.print_activities_top()
        self.print_coffee_stands()
        self.print_emoloyees()
        self.print_products()
        self.print_suppliers()
        self.print_activities_bottom()


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
