from django.shortcuts import render,redirect
from .models import Prescription,DoctorUser,SharedDocument
from patients.models import PatientUser
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import DoctorRegisterForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
     user = request.user
     if DoctorUser.objects.filter(user=user).exists():
      return render(request, 'doctors/dochome.html')
     else:
         return redirect('home')


def RegisterDoc(request):
    if request.method=="POST":
         form = DoctorRegisterForm(request.POST,request.FILES)
         if form.is_valid():
             user_instance = form.save()
             doctor_user = DoctorUser.objects.create(user=user_instance,license=form.cleaned_data['license'],phone_number = form.cleaned_data['phone_number'],name = form.cleaned_data['name'])
             #messages.success(request,f'Account created for {username}')
             return redirect('home')
    else:
         form = DoctorRegisterForm()
    return render(request,'doctors/DocRegister.html',{'form':form})

@login_required
def redirect_user(request):
    user = request.user

    # Check if the user is a doctor
    if DoctorUser.objects.filter(user=user).exists():
        return render(request,'doctors/Dochome.html')
    elif PatientUser.objects.filter(user=user).exists():
        return render(request,'patients/pathome.html')
    # If user is not a doctor or patient, redirect to a generic dashboard or homepage
    else:
        return redirect('home')

class UploadPrescription(CreateView):
    model = Prescription
    fields = ['patientName', 'patientID', 'author', 'followUpDate', 'file',]
    success_url = reverse_lazy('presupload')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.all()
        return context
    

@login_required
def shared_documents(request):
    doctor = request.user.doctoruser
    shared_docs = SharedDocument.objects.filter(doctor=doctor)
    return render(request, 'doctors/shared_documents.html', {'shared_docs': shared_docs})
