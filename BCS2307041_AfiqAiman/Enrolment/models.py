from django.db import models

# Create your models here.
class Student (models.Model) :
    student_ID = models.CharField(max_length=5, primary_key=True)
    Name = models.CharField(max_length=100)
    Course = models.CharField(max_length=3)
    Phone = models.CharField(max_length=12)
    Status = models.CharField(max_length=100, default='Active')

class Activities (models.Model) :
    Activity_id = models.CharField(max_length=5, primary_key=True)
    Activity_name = models.CharField(max_length=100)
    Day = models.CharField(max_length=100)
    Time = models.CharField(max_length=50)

class Enrollment (models.Model) :
    Enrollment_id = models.CharField(max_length=5, primary_key=True)
    Activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Enrollment_Date = models.DateField()


    