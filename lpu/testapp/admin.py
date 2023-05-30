from django.contrib import admin
from testapp.models import *

# Register your models here.
class adminpackages(admin.ModelAdmin):
    list_display=['name','add','percentage','package']
admin.site.register(packages,adminpackages)

class adminlogin(admin.ModelAdmin):
    list_display=['name','email','password']
admin.site.register(loginclass,adminlogin)