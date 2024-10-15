from django.db import models

# Create your models here.
class Mentor(models.Model) :
    mentorid = models.CharField(max_length=10, primary_key=True)
    mentorname = models.CharField(max_length=100,null=True)
    mentorcourse = models.CharField(max_length=5, null=True)
    mentorphonenum = models.CharField(max_length=20, null=True)
    mentoremail = models.CharField(max_length=50,null=True)
    mentorpassword = models.CharField(max_length=20, null=True)

class Student (models.Model) :
    studentid = models.CharField(max_length=15, primary_key=True)
    studentmentorid = models.ForeignKey(Mentor, on_delete=models.CASCADE, null=True)
    studentname = models.CharField(max_length=100, null=True)
    studentcourse = models.CharField(max_length=5, null=True)
    studentphonenum = models.CharField(max_length = 20, null=True)
    studentemail = models.CharField(max_length=100, null=True)
    studentpassword = models.CharField(max_length = 20, null=True)

class Subject(models.Model) :
    subjectcode = models.CharField(max_length=10, primary_key=True)
    subjectname = models.CharField(max_length=100, null=True)

class Tuition (models.Model) :
    tuitioncode = models.CharField(max_length=5, primary_key=True)
    tuitionstudentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    tuitionmentorid = models.ForeignKey(Mentor, on_delete= models.CASCADE)
    subjectcode = models.ForeignKey(Subject, on_delete= models.CASCADE)
    tuitionmeet = models.TextField(max_length=200, null=True)
    tuitiondate = models.DateField(null=True)
    tuitionduration = models.IntegerField(null=True)
    description = models.TextField(max_length=1000, null=True)
