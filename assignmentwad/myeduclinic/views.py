from django.shortcuts import render
from myeduclinic.models import Mentor, Student, Subject, Tuition
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
# Create your views here.
def login (request) : 
    return render (request, "login.html")

def signup(request):
    return render(request, 'signup.html')

def signupstudent(request):
    if request.method == "POST":
        studentid1 = request.POST["studentid"]
        studentname1 = request.POST["studentname"]
        studentemail1 = request.POST["studentemail"]
        studentpassword1 = request.POST["studentpassword"]

        
        new_student = Student(studentid=studentid1, studentname=studentname1,studentemail=studentemail1,studentpassword=studentpassword1)
        new_student.save()

        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "signupstudent.html")
    
def signupmentor (request) : 
    if request.method == "POST" :
        mentorid1 = request.POST["mentorid"]
        mentorname1 = request.POST["mentorname"]
        mentoremail1 = request.POST["mentoremail"]
        mentorpassword1 = request.POST["mentorpassword"]

        datasignupmentor = Mentor(mentorid = mentorid1, mentorname = mentorname1, mentoremail = mentoremail1, mentorpassword = mentorpassword1)
        datasignupmentor.save()

        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "signupmentor.html")
    
def signinstudent (request) : 
    if request.method == "POST" :
        studentemail2 = request.POST["studentemail"]
        studentpassword2 = request.POST["studentpassword"]

        signupstudent = Student.objects.filter(studentemail = studentemail2, studentpassword = studentpassword2)
        
        if signupstudent :
            return HttpResponseRedirect('studenthomepage')
        else :
            return render(request, 'signinstudent.html', {'error' : 'Invalid Credentials'})
        
    return render(request, 'signinstudent.html')

def signinmentor (request) : 
    if request.method == "POST" :
        mentoremail2  = request.POST["mentoremail"]
        mentorpassword2 = request.POST["mentorpassword"]

        signupmentor = Mentor.objects.filter(mentoremail = mentoremail2, mentorpassword = mentorpassword2)

        if signupmentor : 
            return HttpResponseRedirect('mentorhomepage')
        else : 
            return render(request, 'signinmentor.html', {'error' : 'Invalid Credentials'})
        
    return render(request, "signinmentor.html")

def studenthomepage(request):
    if request.method == "POST" :
        mystudentname = request.GET["studentname"]

        mystudent = Student.objects.filter(studentname = mystudentname)

        context = {
            'mystudent' : mystudent 
        }
        return render(request, "studenthomepage.html")

def mentorhomepage(request):
    return render(request, 'mentorhomepage.html')