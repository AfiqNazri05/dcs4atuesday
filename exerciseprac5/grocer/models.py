from django.db import models

# Create your models here.
class Supplier (models.Model) :
    suppid = models.CharField(max_length=10, primary_key=True)
    suppname = models.CharField