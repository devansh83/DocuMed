from django.db import models
from django.contrib.auth.models import User
class Prescription(models.Model):
    patientName = models.CharField(max_length=100)
    patientID = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    followUpDate = models.DateField()
    file = models.FileField(upload_to='')