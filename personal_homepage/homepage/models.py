from django.db import models

# Create your models here.
class Programme (models.Model) :
    programmmecode = models.CharField(max_length=10, primary_key=True)
    programmename = models.CharField(max_length=100)
    programmeaccdate = models.DateField()

class Mentor (models.Model) :
    mentorid = models.CharField(max_length= 10, primary_key=True)
    mentorname = models.CharField(max_length=100)
    mentoremail = models.CharField(max_length=100)

class Student (models.Model) :
    studentid = models.CharField(max_length=5, primary_key=True)
    studentname = models.CharField(max_length=100)
    studentemail = models.CharField(max_length=100, null=True)
    studentage = models.IntegerField(default=1)
    mentorid = models.ForeignKey(Mentor, on_delete=models.CASCADE, null=True)