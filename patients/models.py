from django.db import models
from django.contrib.auth.models import User

DOCUMENT_TYPES = (
    ('prescription', 'Prescription'),
    ('lab_report', 'Lab Report'),
    ('scans', 'Scans'),
    ('medical_certificate', 'Medical Certificate'),
)

class PatientUser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    USERNAME_FIELD = 'username'

class Medication(models.Model):
    medical_condition = models.CharField(max_length=100)
    medicines = models.TextField()
    author = models.ForeignKey(PatientUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')    

class Documents(models.Model):
    author = models.ForeignKey(PatientUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')
    type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
   