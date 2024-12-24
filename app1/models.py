from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name

class Address(models.Model):
    customer=models.ForeignKey(Customer, related_name='addresses',on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    lat=models.CharField(max_length=10, null=True,blank=True)
    lng=models.CharField(max_length=10, null=True,blank=True)
    img_url=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.address

class Service(models.Model):
    address=models.ForeignKey(Address, related_name='services',on_delete=models.CASCADE)
    keluhan=models.CharField(max_length=200)
    tindakan=models.CharField(max_length=200)
    hasil=models.CharField(max_length=200)
    service_date=models.DateField()
    img_url=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.keluhan
