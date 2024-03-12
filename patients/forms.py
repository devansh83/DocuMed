from django import forms
from django.contrib.auth.models import User
from .models import PatientUser
from django.contrib.auth.forms import UserCreationForm

class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    phone_number = forms.IntegerField(max_value=9999999999, min_value=1000000000)
   

    class Meta:
        model=User
        fields= ['username','name','phone_number','email','password1','password2']
    