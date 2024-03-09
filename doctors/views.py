from django.shortcuts import render
from .models import Prescription
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'doctors/home.html')

class UploadPrescription(CreateView):
    model = Prescription
    fields = ['patientName', 'patientID', 'author', 'followUpDate', 'file',]
    success_url = reverse_lazy('presupload')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.all()
        return context