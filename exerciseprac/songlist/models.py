from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Singer (models.Model) :
    singerid = models.CharField(max_length=3, primary_key=True)
    singername = models.CharField(max_length=100)
    singerorigin = models.CharField(max_length=100)

class Album (models.Model) :
    albumname = models.CharField(max_length=100)
    singerid = models.ForeignKey(Singer, on_delete=models.CASCADE)
    albumyear = models.IntegerField()

class Song (models.Model) :
    songid = models.CharField(max_length=5, primary_key=True)
    albumid = models.ForeignKey(Album, on_delete= models.CASCADE)
    songname = models.CharField(max_length=100)
    minutes = models.IntegerField()