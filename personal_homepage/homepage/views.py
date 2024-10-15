from django.shortcuts import render, get_object_or_404
from homepage.models import Programme, Mentor, Student
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def index(request):
    myprogramme = Programme.objects.all().values()
    mymentor = Mentor.objects.all().values()
    context = {
        'studentname': "Afiq",
        'myprogramme': myprogramme,
        'mymentor': mymentor
    }
    return render(request, "index.html", context)

def newmentor(request):
    displaydata = Mentor.objects.all().values()
    if request.method == "POST":
        menid1 = request.POST['mentorid']
        menname1 = request.POST['mentorname']
        menemail1 = request.POST['mentoremail']
        data = Mentor(mentorid=menid1, mentorname=menname1, mentoremail=menemail1)
        data.save()

        context = {
            'displaydata': displaydata,
            'message': 'NEW MENTOR HAS BEEN SAVED'
        }

        return render(request, "newmentor.html", context)
    else:
        dict = {
            'message': 'No POST Method Activated',
            'displaydata': displaydata,
        }

        return render(request, "newmentor.html", dict)

def newstudent(request):
    mymentor = Mentor.objects.all().values()
    if request.method == "POST":
        studentid1 = request.POST["studentid"]
        studentname1 = request.POST["studentname"]
        studentemail1 = request.POST["studentemail"]
        studentage1 = request.POST["studentage"]
        mentorid1 = request.POST["mentorid"]

        # Get the mentor instance
        mentornew = Mentor.objects.get(mentorid=mentorid1)

        # Create and save the new student instance
        data = Student(studentid=studentid1, studentname=studentname1, studentemail=studentemail1, studentage=studentage1, mentorid=mentornew)
        data.save()

        # Re-fetch the student data to show the updated list
        studmentor1 = Student.objects.all().values()

        context = {
            'studmentor1': studmentor1,
            'mymentor': mymentor,
            'message': 'NEW STUDENT HAS BEEN SAVED'
        }
        return render(request, "newstudent.html", context)
    else:
        # Fetch the student and mentor data when GET request is made
        studmentor1 = Student.objects.all().values()
        context = {
            'studmentor1': studmentor1,
            'mymentor': mymentor,
            'message': 'Page is refreshed',
        }
        return render(request, "newstudent.html", context)

def updatementor(request, mentorid):
    updateid = Mentor.objects.get(mentorid=mentorid)
    mymentor = Mentor.objects.all()
    dict = {
        'updateid': updateid,
        'mymentor': mymentor,
        'message': 'PAGE RENDERED, DATA IS NOT UPDATED YET'
    }
    return render(request, "updatementor.html", dict)

def updatedata(request, mentorid):
    data = Mentor.objects.get(mentorid=mentorid)
    mentorname = request.POST['mentorname']
    mentoremail = request.POST['mentoremail']
    data.mentorname = mentorname
    data.mentoremail = mentoremail
    data.save()

    return HttpResponseRedirect(reverse("index"))

def updatestudent(request, studentid):
    updateid = Student.objects.get(studentid=studentid)
    dict = {
        'updateid': updateid,
        'message': 'PAGE RENDERED, DATA IS NOT UPDATED YET'
    }
    return render(request, "updatestudent.html", dict)

def updatedatastudent(request, studentid):
    if request.method == "POST":
        data = Student.objects.get(studentid=studentid)
        studentname = request.POST['studentname']
        studentemail = request.POST['studentemail']
        studentage = request.POST['studentage']
        mentorid1 = request.POST["mentorid"]
        mentornew = Mentor.objects.get(mentorid=mentorid1)

        data.studentname = studentname
        data.studentemail = studentemail
        data.studentage = studentage
        data.mentorid = mentornew
        data.save()

        return HttpResponseRedirect(reverse("newstudent"))

def deletementor(request,mentorid):
    datanakdelete = Mentor.objects.get(mentorid = mentorid)
    dict = {
        'datatobedeleted' : datanakdelete
    }
    return render(request,"deletementor.html",dict)



def delete(request,mentorid):
    deletementor = Mentor.objects.get(mentorid=mentorid)
    deletementor.delete()
    return HttpResponseRedirect(reverse("index"))

def searchmentor(request):
    query = request.GET.get('search')  # Fetch the query from the search box
    if query:
        # Perform case-insensitive search on mentor ID and name
        findmentor = Mentor.objects.filter(
            Q(mentorid__icontains=query) | Q(mentorname__icontains=query)
        )
    else:
        findmentor = Mentor.objects.none()  # Empty queryset if no search term

    dict = {
        'findmentor': findmentor
    }
    return render(request, 'searchmentor.html', dict)