touimport csv
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))
        return students
    
    # end original data

    """
Staff class
"""
import csv
from .user import User


class Staff(User):
    @classmethod
    def load_all_staff(cls):
        all_staff = []
        with open('./data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                new_staff = cls(**row)
                all_staff.append(new_staff)

            return all_staff

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, employee_id, password, role)
        # self.name = name
        # self.age = age
        # self.role = role
        # self.employee_id = employee_id
        # self.password = password

    def __repr__(self):
        return f"{self.name} | {self.age} | {self.role} | {self.employee_id} | {self.password}"

    # We need a getter and setter for employee_id
    # because the User class just has id, since User is inherited by both
    # Student and Staff
    @property
    def employee_id(self):
        return self.id

    @employee_id.setter
    def employee_id(self, new_id):
         self.id = new_id



