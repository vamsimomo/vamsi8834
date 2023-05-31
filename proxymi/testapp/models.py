from django.db import models
from django.db.models.query import QuerySet

# Create your models here.
class custommanager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)
class custommanager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=14000)
class custommanager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')

class Employee(models.Model):
    ename=models.CharField(max_length=64)
    eno=models.IntegerField()
    esal=models.FloatField()
    eaddr=models.CharField(max_length=130)
    objects=custommanager1()

class proxyEmployee1(Employee):
    objects=custommanager2()
    class Meta:
        proxy=True
class proxyEmployee2(Employee):
    objects=custommanager3()
    class Meta:
        proxy=True