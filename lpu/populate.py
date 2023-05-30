import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','lpu.settings')
import django
django.setup()
from testapp.models import packages
from faker import Faker
from random import *
fake = Faker()
def populate(n):
    for i in range(n):
        fpackage = randint(1000000,9000000)
        fename = fake.name()
        fper = randint(70,100)
        feaddr = fake.city()
        emp_record = packages.objects.get_or_create(
            percentage=fper,
            name = fename,
            add = feaddr,
            package=fpackage)
n = int(input("Enter number of records:"))
populate(n)
print(f'{n} Records inserted successfully......')