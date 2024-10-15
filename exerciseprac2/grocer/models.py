from django.db import models

# Create your models here.
class Supplier (models.Model) :
    suppid = models.CharField(max_length=4, primary_key=True)
    suppname = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)

class Product (models.Model) :
    proid = models.CharField(max_length=3, primary_key=True)
    prodescription = models.CharField(max_length=100)

class Supplier_Product (models.Model) :
    suppid = models.ForeignKey(Supplier, on_delete= models.CASCADE)
    proid = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)