# The Repository
from DAOs import _CoffeeStands, _Employees, _Suppliers, _Activities, _Products
import sqlite3
import atexit
import os  # for remove # TODO: ALON 1320 remember to delete the line!


# The Repository

class _Repository:
    def __init__(self):

        # todo: change logic to check first if it exist, then create a fresh one
        DBExist = os.path.isfile('moncafe.db')
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
                CREATE TABLE students (id   INT   PRIMARY KEY,
                                       name TEXT  NOT NULL
                );

                CREATE TABLE assignments (num             INT     PRIMARY KEY,
                                          expected_output TEXT    NOT NULL
                );

                CREATE TABLE grades (student_id      INT     NOT NULL,
                                     assignment_num  INT     NOT NULL,
                                     grade           INT     NOT NULL,

                                     FOREIGN KEY(student_id)     REFERENCES students(id),
                                     FOREIGN KEY(assignment_num) REFERENCES assignments(num),
                                     PRIMARY KEY (student_id, assignment_num)
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


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
