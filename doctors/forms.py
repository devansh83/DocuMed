from django import forms
from django.contrib.auth.models import User
from .models import DoctorUser
from django.contrib.auth.forms import UserCreationForm

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    phone_number = forms.IntegerField(max_value=9999999999, min_value=0)
    license = forms.FileField()

    class Meta:
        model=User
        fields= ['username','name','phone_number','email','password1','password2','license']
    