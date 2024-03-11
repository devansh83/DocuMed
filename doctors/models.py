from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from patients.models import PatientUser, Documents


class DoctorUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=100)
    license = models.FileField()
    phone_number = models.IntegerField()
    USERNAME_FIELD = 'username'

class Prescription(models.Model):
    patientName = models.CharField(max_length=100)
    patientID = models.CharField(max_length=100)
    author = models.ForeignKey(DoctorUser, on_delete=models.CASCADE)
    followUpDate = models.DateField()
    file = models.FileField(upload_to='')
    
class SharedDocument(models.Model):
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientUser, on_delete=models.CASCADE)


