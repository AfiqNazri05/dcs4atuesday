from django.db import models

# Create your models here.
class Membership (models.Model) :
    membershipid = models.CharField(max_length=5, primary_key=True)
    membershipname = models.CharField(max_length=100)
    emailaddress = models.CharField(max_length=100)

class Movie (models.Model) :
    movieid = models.CharField(max_length=3, primary_key=True)
    movietitle = models.CharField(max_length=100)
    movieduration = models.IntegerField()

class Records (models.Model) :
    rentalcode = models.CharField(max_length=3, primary_key=True)
    membershipid = models.ForeignKey(Membership, on_delete= models.CASCADE)
    movieid = models.ForeignKey(Movie, on_delete= models.CASCADE)
    startdate = models.DateField()
    returndate = models.DateField()
    
     