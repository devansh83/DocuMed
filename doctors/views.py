from django.shortcuts import render,redirect
from .models import Prescription,DoctorUser,SharedDocument,Profile
from patients.models import PatientUser
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import DoctorRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

@login_required
def home(request):
    user=request.user
    doctor = request.user.doctoruser
    shared_docs = SharedDocument.objects.filter(doctor=doctor)
    shared_patients = set([doc.patient for doc in shared_docs])

    context = {
        'shared_docs': shared_docs,
        'shared_patients': shared_patients,
        'user' : user
    }
    
    return render(request, 'doctors/dochome.html', context)
# @login_required
# def home(request):
#      user = request.user
#      if DoctorUser.objects.filter(user=user).exists():
#       return render(request, 'doctors/dochome.html')
#      else:
#          return redirect('home')


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
        # return render(request,'doctors/Dochome.html')
        return redirect('doctor:doctor-home')
    elif PatientUser.objects.filter(user=user).exists():
        # return render(request,'patients/pathome.html')
        return redirect('patient:patient-home')
    # If user is not a doctor or patient, redirect to a generic dashboard or homepage
    else:
        return redirect('home')

class UploadPrescription(LoginRequiredMixin, CreateView):
    model = Prescription
    fields = ['patientName', 'patientID', 'followUpDate', 'file',]
    success_url = reverse_lazy('presupload')
    login_url = '/doctor/login/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user.doctoruser
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.all()
        return context
    

# @login_required
# def shared_documents(request):
#     doctor = request.user.doctoruser
#     shared_docs = SharedDocument.objects.filter(doctor=doctor)
#     return render(request, 'doctors/shared_documents.html', {'shared_docs': shared_docs})

@login_required
def shared_documents(request):
    user = request.user
    if not DoctorUser.objects.filter(user=user).exists():
        return redirect('login')
    doctor = request.user.doctoruser
    shared_docs = SharedDocument.objects.filter(doctor=doctor)
    shared_patients = set([doc.patient for doc in shared_docs])

    context = {
        'shared_patients': shared_patients,
        'shared_docs': shared_docs,
    }

    return render(request, 'doctors/shared_documents.html', context)


@login_required
def patient_documents(request, patient_name):
    user = request.user
    if not DoctorUser.objects.filter(user=user).exists():
        return redirect('login')
    patient = get_object_or_404(PatientUser, name=patient_name)
    shared_docs = SharedDocument.objects.filter(patient=patient, doctor=request.user.doctoruser)

    context = {
        'patient': patient,
        'shared_docs': shared_docs,
    }

    return render(request, 'doctors/patient_documents.html', context)

@login_required
def profile(request,doctor_id):
    # user = request.user
    # if not DoctorUser.objects.filter(user=user).exists():
    #     return redirect('login')
    # doctor = request.user.doctoruser
    doctor=get_object_or_404(DoctorUser, user__username=doctor_id)
    profile = Profile.objects.get(doctor_user=doctor)

    context = {
        'profile' : profile, 
    }
    return render(request,'doctors/profile.html',context)