from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=100) 
    personal_email = models.EmailField(max_length=100)
    locker_number = models.IntegerField()
    locker_combination = models.CharField()
    good_student = models.BooleanField()