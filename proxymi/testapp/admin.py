from django.contrib import admin
from testapp.models import *
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename','eno','esal','eaddr']
class proxyadmin1(admin.ModelAdmin):
    list_display=['ename','eno','esal','eaddr']
class proxyadmin2(admin.ModelAdmin):
    list_display=['ename','eno','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(proxyEmployee1,proxyadmin1)
admin.site.register(proxyEmployee2,proxyadmin2)