from django.shortcuts import render
from .models import Medication, Documents
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def home(request):
    # context = {
    #     'medications': Medication.objects.all(),
    #     'documents': Documents.objects.all()
    # }
    return render(request, 'patients/home.html')


class UploadMedication(CreateView):
    model = Medication
    fields = ['medical_condition', 'medicines', 'file', 'author']
    success_url = reverse_lazy('medupload')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medications'] = Medication.objects.all()
        return context
    
class UploadDocuments(CreateView):
    model = Documents
    fields = ['file', 'author']
    success_url = reverse_lazy('docupload')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Documents.objects.all()
        return context