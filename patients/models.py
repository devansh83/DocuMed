from django.db import models
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')
   