# Data Transfer Objects:
class CoffeeStand:
    def __init__(self, stand_id, emp):
        self.stand_id = stand_id
        self.emp = emp


class Employee:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier:
    def __init__(self, sup_id, sup_name, sup_contact_info ):
        self.sup_id = sup_id
        self.sup_name = sup_name
        self.sup_contact_info = sup_contact_info


class Product:
    def __init__(self, student_id, assignment_num, grade):
        self.student_id = student_id
        self.assignment_num = assignment_num
        self.grade = grade


class Activity:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand
