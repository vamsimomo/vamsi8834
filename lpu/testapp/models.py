from django.db import models

# Create your models here.
class packages(models.Model):
    name=models.CharField(max_length=120)
    add=models.CharField(max_length=120)
    percentage=models.FloatField()
    package=models.IntegerField()

class loginclass(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=10)
