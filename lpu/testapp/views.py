from django.shortcuts import render,redirect
from testapp.forms import myform
from testapp.models import packages,loginclass
from testapp.forms import loginform,myform
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'testapp/index.html')
def insidehome(request):
    return render(request,'testapp/insidehome.html')
def myviewform(request):
    form =myform
    return render(request,'testapp/login.html',{'form':form})
def my_view(request):
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            course=form.cleaned_data['course']
            select_programme=form.cleaned_data['select_programme']
            return render(request,'testapp/login.html', {'name': name})
    else:
        form =myform()
    return render(request,'testapp/login.html',{'form': form})
def sports(request):
    return render(request,'testapp/sports.html')
def recuireters(request):
    return render(request,'testapp/requireters.html')
def recuiretersdata(request):
    list_details=packages.objects.all()
    return render(request,'testapp/requireters.html',{'list_details':list_details})
def Career_Support_view(request):
    return render(request,'testapp/CareerSupport.html')
def programmers(request):
    return render(request,'testapp/programmers.html')
def viewlogin(request):
    if request.method=='POST':
        form =loginform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.changed_data['email']
            password=form.cleaned_data['password']
            my_dict={'name':name,'email':email,'password':password}
            return render(request, 'testapp/viewlogin.html', {'my_dict': my_dict})
    else:
        form =loginform()
    return render(request,'testapp/viewlogin.html',{'form': form})
def highlites(request):
    return render(request,'testapp/highlites.html')
def loginthanx(request):
    name_list=loginclass.objects.name()
    return render(request,'testapp/loginthanx.html',{'name_list':name_list})
def submit_form(request):
    return redirect('afterregistration')
def afterregistration(request):
    name_login = loginclass.objects.name()
    return render(request, 'testapp/afterregistration.html', {'name_login': name_login, 'message': 'Thank you!'})
