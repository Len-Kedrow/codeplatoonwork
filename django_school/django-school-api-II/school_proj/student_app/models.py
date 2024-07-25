from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, unique=False)
    student_email = models.EmailField(null = False, blank = False, unique=True)
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default=1, null = False, blank = False, unique=True, db_default=110)
    locker_combination = models.CharField(max_length=255, null = False, blank = False, unique=False, db_default="12-12-12")
    good_student = models.BooleanField(unique=False, db_default=True)