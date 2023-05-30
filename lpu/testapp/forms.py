from django import forms

class myform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField()
    course=forms.CharField()
    select_programme=forms.CharField()

class loginform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()