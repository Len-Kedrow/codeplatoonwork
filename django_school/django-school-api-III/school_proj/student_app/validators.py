import re
from django.core.exceptions import ValidationError



def validate_name(name):
    name_pattern = r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$'
    if not re.match(name_pattern, name):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"' )
    
def validate_locker_num(num):
    if num < 1: 
        raise ValidationError("Ensure this value is greater than or equal to 1.")
    if num > 200:
        raise ValidationError("Ensure this value is less than or equal to 200.")
    



def validate_student_email(student_email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@school\.com$"
    if not re.match(email_pattern ,student_email):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_combination(combination):
    combo_pattern = r"^\d{2}-\d{2}-\d{2}$"
    if not re.match(combo_pattern,combination):
        raise ValidationError('Combination must be in the format "12-12-12"')
    

