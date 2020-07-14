from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    major = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)