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
               INSERT INTO Coffee stands (id, location, #emp) VALUES (?, ?, ?)
           """, [coffee_stand.id, coffee_stand.location, coffee_stand.emp])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM Coffee stands WHERE id = ?
        """, [coffee_stand_id])

        return CoffeeStand(*c.fetchone())

    def print_cStands(self):
        print("Coffee stands")



class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
                INSERT INTO Employees (num, expected_output) VALUES (?, ?, ?, ?)
        """, [employee.employee_id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, name, salary, coffee-stand FROM Employees WHERE id = ?
            """, [employee_id])

        return Employee(*c.fetchone())

    def print_emoloyees(self):
        print("Coffee stands")


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
            INSERT INTO Suppliers (id, name, contact_info) VALUES (?, ?, ?)
        """, [supplier.sup_id, supplier.sup_name, supplier.sup_contact_info])

    # TODO: change method: here because of copying from class, not sure if needed (same for all findAll()
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT student_id, assignment_num, grade FROM Suppliers
        """).fetchall()

        return [Supplier(*row) for row in all]

    def print_suppliers(self):
        print("Coffee stands")


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?)
        """, [product.product_id, product.product_description, product.product_price, product.product_quantity])

    # TODO: change method: here because of copying from class, not sure if needed (same for all findAll()
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, description, price, quantity FROM Products
        """).fetchall()

        return [Product(*row) for row in all]

    def print_products(self):
        print("Coffee stands")


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

        return [Activity(*row) for row in all]
