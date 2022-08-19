from django.db import models
from django import forms
# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    balance=models.IntegerField()

# Create your models here.
