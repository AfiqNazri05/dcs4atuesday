from django.db import models

# Create your models here.
class Vehicle(models.Model):
    platno = models. CharField (max_length=10 , primary_key=True)
    company = models.CharField(max_length=60)
    capacity = models. IntegerField(null=True)
    datepurchased = models.DateField(null=True)

class Customer (models. Model):
    custic = models. CharField(max_length=60 , primary_key=True)
    custname = models. CharField(max_length=60)
    custphone = models. IntegerField(null=True)
    custemail = models. CharField (max_length=60)

class Booking(models.Model): 
    platno = models. ForeignKey (Vehicle, on_delete=models.CASCADE)
    custic = models. ForeignKey (Customer, on_delete=models.CASCADE)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    totalcost = models. IntegerField(null=True)