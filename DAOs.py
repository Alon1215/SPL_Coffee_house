# Data Access Objects:
# All of these are meant to be singletons
from DTOs import *
import sqlite3


# TODO: change/add methods: here because of copying from class, not sure what is needed

class _CoffeeStands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
               INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
           """, [coffee_stand.stand_id, coffee_stand.location, coffee_stand.emp])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM Coffee_stands WHERE id = ?
        """, [coffee_stand_id])

        return CoffeeStand(*c.fetchone())


class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
                INSERT INTO Employees (id, name,salary,coffee_stand) VALUES (?, ?, ?, ?)
        """, [employee.employee_id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, name, salary, coffee-stand FROM Employees WHERE id = ?
            """, [employee_id])

        return Employee(*c.fetchone())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
            INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.sup_id, supplier.sup_name, supplier.sup_contact_info])

    # TODO: change method: here because of copying from class, not sure if needed (same for all findAll()
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT student_id, assignment_num, grade FROM Suppliers
        """).fetchall()

        return [Supplier(*row) for row in all]


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.product_id, product.product_description, product.product_price, product.product_quantity])

    # TODO: change method: here because of copying from class, not sure if needed (same for all findAll()
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT product_id, description, price, quantity FROM Products
        """).fetchall()

        return [Product(*row) for row in all]

    def update_quantity(self, product_id, new_quantity):
        c = self._conn.cursor()
        c.execute("""
            UPDATE Products SET quantity=(?) 
            WHERE id=(?)
            """, [new_quantity, product_id])

    def get_quantity(self, product_id):
        p = self.find(product_id)
        return p.product_quantity

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
                   SELECT id,description,price,quantity  FROM  Products WHERE id=(?)
                    """, [product_id])
        return Product(*c.fetchone())


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""
            INSERT INTO Activities (Product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    # TODO: change method
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT student_id, assignment_num, grade FROM grades
        """).fetchall()

        return (Activity(*row) for row in all)
