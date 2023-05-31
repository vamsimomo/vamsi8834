from django.shortcuts import render
from testapp.models import *

# Create your views here.
def employeeview(request):
    emp_list=proxyEmployee1.objects.all()
    #emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})