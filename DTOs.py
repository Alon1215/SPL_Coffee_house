# Data Transfer Objects:
class CoffeeStand:
    def __init__(self, stand_id, location, emp):
        self.stand_id = stand_id
        self.location = location
        self.emp = emp


class Employee:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Product:
    def __init__(self, product_id, product_description, product_price, product_quantity):
        self.product_id = product_id
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity


class Supplier:
    def __init__(self, sup_id, sup_name, sup_contact_info):
        self.sup_id = sup_id
        self.sup_name = sup_name
        self.sup_contact_info = sup_contact_info


class Activity:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date
