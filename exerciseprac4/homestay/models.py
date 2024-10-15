from django.db import models

# Create your models here.
class Client(models.Model) :
    clientid = models.CharField(max_length=10, primary_key=True)
    clientname = models.CharField(max_length=100)
    contactdetails = models.CharField(max_length=100)

class Apartment(models.Model) :
    houseno = models.CharField(max_length=4, primary_key=True)
    housedescription = models.CharField(max_length=100)
    pernight = models.IntegerField()
    status = models.CharField(max_length=100, default='Active')

class Booking(models.Model) :
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    houseno = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    