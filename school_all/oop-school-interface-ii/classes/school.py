from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
####end original data

# """
# School class
# """

# class School:
#     def __init__(self, name): 
#         self.name = name
#         # TODO: make real
#         self.students = []
#         self.staff = []

#     def __repr__(self):
#         return self.name