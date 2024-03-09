from django.db import models
from django.contrib.auth.models import User

class Medication(models.Model):
    medical_condition = models.CharField(max_length=100)
    medicines = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')

class Documents(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')