from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class DoctorUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True)
   # username = models.CharField(max_length=200)
   # password = models.CharField(max_length=200,default = 'none')
    name = models.CharField(max_length=100)
    license = models.FileField()
    phone_number = models.IntegerField()
    USERNAME_FIELD = 'username'
   # def set_password(self, password):
     #  self.password = make_password(password)


class Prescription(models.Model):
    patientName = models.CharField(max_length=100)
    patientID = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    followUpDate = models.DateField()
    file = models.FileField(upload_to='')


