from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model 


class parking1(models.Model):
    fullname= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    flatnumber= models.CharField(max_length=100)
    parkingno= models.CharField(max_length=100)
    pourchno= models.CharField(max_length=100 , unique=True)
    


    def __str__(self):
        return str(self.id)


class parking2(models.Model):
    fullname= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    flatnumber= models.CharField(max_length=100)
    parkingno= models.CharField(max_length=100)
    pourchno= models.CharField(max_length=100)


    def __str__(self):
        return str(self.id)



class parking3(models.Model):
    fullname= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    flatnumber= models.CharField(max_length=100)
    parkingno= models.CharField(max_length=100)
    pourchno= models.CharField(max_length=100)


    def __str__(self):
        return str(self.id)


class parking4(models.Model):
    fullname= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    flatnumber= models.CharField(max_length=100)
    parkingno= models.CharField(max_length=100)
    pourchno= models.CharField(max_length=100)


    def __str__(self):
        return str(self.id)


class overalldata(models.Model):
    fullname= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    flatnumber= models.CharField(max_length=100)
    parkingno= models.CharField(max_length=100)
    pourchno= models.CharField(max_length=100)


    def __str__(self):
        return str(self.id)