class Student:
    def __init__(self, name, age=13, grade="12th"): 
            self._name = name
            self._age = age
            self._grade = grade 
             
           
                       
            
            def __str__(self):
                
                return f"This student name is {self.get_name} they are {self.get_age} and they are in {self.grade}."
            
            def advance(self, years_advanced):
                return f"{self.get_name} is advancing to {years_advanced} grade"
            
            def study(self, subject): 
                return f"{self.get_name} is learning {subject}"  
                


 # Getter for name attribute
    @property
    def get_name(self):
        return self._name

    # Setter for name attribute
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string.")

    # Getter for age attribute
    @property
    def get_age(self):
        return self._age

    # Setter for age attribute
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer.")
    
    @property
    def get_grade(self):
        return self._grade

    # Setter for name attribute
    @get_grade.setter
    def set_grade(self, new_grade):

        if isinstance(new_grade, str) and int(new_grade[0:2] )<= 12:
            self._grade = new_grade
        else:
            print("Grade must be a string.")

student = Student("Bob", 35, 4)

print(f" This guys name is {student.get_name} and they are {student.get_age}.")

student.set_name="David"
print(f" This guys name is {student.get_name} and they are {student.get_age}.")

