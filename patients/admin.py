from django.contrib import admin
from .models import Medication, Documents,PatientUser


admin.site.register(Medication)
admin.site.register(Documents)
admin.site.register(PatientUser)


