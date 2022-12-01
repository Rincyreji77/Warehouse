from email.mime import image
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20) 
    email = models.EmailField()  
    phone = models.CharField(max_length=100)  
    desc = models.CharField(max_length=15)
    def __str__(self):
        return self.name


class AddProduct(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=20) 
    image = models.CharField(max_length=1000)  
    stock = models.IntegerField()  
    price = models.FloatField()
    def __str__(self):
        return self.name

class Purchase(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    item = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField()
    delivery = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    item = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField()
    
