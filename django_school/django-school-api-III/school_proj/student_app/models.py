from django.db import models
from django.core import validators as v
from .validators import (
    validate_combination,
    validate_name,
    validate_student_email,
    validate_locker_num
)

# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, null = False, blank = False, validators=[validate_name])
    student_email = models.EmailField(
        null = False, blank = False, unique=True, validators=[validate_student_email])
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default = 110, null = False, blank = False, unique=True, validators=[validate_locker_num])
    locker_combination = models.CharField( 
        default="12-12-12",null = False, blank = False,max_length=255, validators=[validate_combination] )
    good_student = models.BooleanField(default=True)