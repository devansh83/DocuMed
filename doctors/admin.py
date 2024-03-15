from django.contrib import admin
from .models import Prescription
from .models import DoctorUser,SharedDocument,Profile,Day

admin.site.register(Prescription)
admin.site.register(DoctorUser)
admin.site.register(SharedDocument)
admin.site.register(Profile)
admin.site.register(Day)
