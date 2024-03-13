from django.shortcuts import render

from django.http import HttpResponse
from doctors.models import DoctorUser


def home(request):
    return render(request, 'loginorreg.html')

def land(request):
    return render(request,'home.html')




