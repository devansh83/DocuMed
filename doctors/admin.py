from django.contrib import admin
from .models import Prescription
from .models import DoctorUser

admin.site.register(Prescription)
admin.site.register(DoctorUser)
