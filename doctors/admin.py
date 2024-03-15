from django.contrib import admin
from .models import Prescription
from .models import DoctorUser,Day,Profile

admin.site.register(Prescription)
admin.site.register(DoctorUser)
admin.site.register(Day)
admin.site.register(Profile)
