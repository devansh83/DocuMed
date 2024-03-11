from django.shortcuts import render,redirect
from .models import Medication, Documents,PatientUser
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PatientRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
     user = request.user
     if PatientUser.objects.filter(user=user).exists():
      return render(request, 'patients/pathome.html')
     else:
         return redirect('home')


def RegisterPatient(request):
    if request.method=="POST":
         form = PatientRegisterForm(request.POST)
         if form.is_valid():
             user_instance = form.save()
             patient_user = PatientUser.objects.create(user=user_instance,phone_number = form.cleaned_data['phone_number'],name = form.cleaned_data['name'])
             #messages.success(request,f'Account created for {username}')
             return redirect('home')
    else:
         form = PatientRegisterForm()
    return render(request,'patients/patientreg.html',{'form':form})

"""
@login_required
def redirect_user(request):
    user = request.user

    # Check if the user is a doctor
    if PatientUser.objects.filter(user=user).exists():
        return render(request,'patients/pathome.html')

    # If user is not a doctor or patient, redirect to a generic dashboard or homepage
    else:
        return redirect('home')
"""


class UploadMedication(CreateView):
    model = Medication
    fields = ['medical_condition', 'medicines', 'file', 'author']
    success_url = reverse_lazy('medupload')
    
    @login_required
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medications'] = Medication.objects.all()
        return context
    
class UploadDocuments(CreateView):
    model = Documents
    fields = ['file', 'author']
    success_url = reverse_lazy('docupload')
    
    @login_required
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Documents.objects.all()
        return context