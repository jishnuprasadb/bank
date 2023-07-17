from django.db import models

# Create your models here.
class Bank(models.Model):
    name=models.CharField(max_length=200)
    date_birth=models.DateField(auto_now=True)
    age=models.CharField(max_length=250)
    gender=models.CharField(max_length=200)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    address=models.TextField()
    district=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    account_type=models.CharField(max_length=250)
    materials=models.CharField(max_length=250)

