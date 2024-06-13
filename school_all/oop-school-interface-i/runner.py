"""
Game plan

X 1. Create a simple School class
X 2. Create a simple Student class
    - name
    - age
    - role
    - school_id (student id)
    - password

X 3. Import all students from csv into our program
    - create a whole bunch of students
X4. Create a simple Staff class
    - name
    - age
    - role
    - employee_id
    - password
X5. Import all Staff from csv into our program
6. Write the command line program

X- TASK: SHOW MAIN UI:
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit

X- 1 List All Students
X - 2 View Individual Student <student_id>
X- 3 Add a Student
X- 4 Remove a Student <student_id>
X- 5 Quit
X- If the user selects an option, once they're done, unless they've quit, show the main menu again

X- Stretch goal: list all staff


X7. Create a User class
X8. Refactor School and Staff to inherit from User
"""

from classes.school import School 
from classes.student import Student
from classes.staff import Staff

ridgemont_high = School('Ridgemont High') 

# print(ridgemont_high)

alice = Student('Alice', 20, 123, 'password')
print(alice)
print(f"ALICE ID TO CHECK IF USER CLASS WAS USED: {alice.id}")
print(alice.am_i_a_user())
bob = Staff('bob', 40, 'Instructor', 1234, 'xyz123')
# print(bob)

ridgemont_high.students = Student.load_all_students()
# print(ridgemont_high.students)

ridgemont_high.staff = Staff.load_all_staff()
print(ridgemont_high.staff)

main_ui_message = f"""
{ridgemont_high.name} Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 List all Staff
    6 Quit
"""

# Command line program code
is_active = True
while is_active:
    cmd = input(main_ui_message) 
    print(f"user input {cmd}")

    # quit
    if cmd == "6":
        print("Quitting program")
        is_active = False
    
    # list all students
    elif cmd == "1":
        print(ridgemont_high.students)

    # view individual student by id
    elif cmd == "2":
        desired_school_id = input("Enter student id you would like information for: ")
        desired_student = None
        for student in ridgemont_high.students:
            if student.school_id == desired_school_id:
                desired_student = student

        if desired_student is None:
            print(f"Student with school_id {desired_school_id} does not exist")   
        else:
            print(desired_student)

    # add a student
    elif cmd == "3":
        info = input("Enter new student info in the following format, separated by commas. Name, Age, School ID, Password: ")
        # TODO: Strip whitespace from each element in list so it doesnt get stored that way
        info = info.split(',')
        new_student = Student(info[0], info[1], info[2], info[3])
        ridgemont_high.students.append(new_student)
        print("Updated student list:")
        print(ridgemont_high.students)

    # remove a student
    elif cmd == "4":
        id_to_del = input("Enter student id you would like to delete: ")
        updated_students = []
        for student in ridgemont_high.students:
            if student.school_id != id_to_del:
                updated_students.append(student)

        ridgemont_high.students = updated_students
        print("Updated student list:")
        print(ridgemont_high.students)

    # list all staff
    elif cmd == "5":
        print(ridgemont_high.staff)

    # error case handle invalid input
    else:
        print("Invalid user input. Please select an option 1 thru 6")

        