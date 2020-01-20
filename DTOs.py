# Data Transfer Objects:
class CoffeeStand:
    def __init__(self, stand_id, emp):
        self._stand_id = stand_id
        self._emp = emp


class Employee:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self._employee_id = employee_id
        self._name = name
        self._salary = salary
        self._coffee_stand = coffee_stand


class Supplier:
    def __init__(self, sup_id, sup_name, sup_contact_info ):
        self._sup_id = sup_id
        self._sup_name = sup_name
        self._sup_contact_info = sup_contact_info


class Product:
    def __init__(self, student_id, assignment_num, grade):
        self._student_id = student_id
        self._assignment_num = assignment_num
        self._grade = grade


class Activity:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self._employee_id = employee_id
        self._name = name
        self._salary = salary
        self._coffee_stand = coffee_stand
