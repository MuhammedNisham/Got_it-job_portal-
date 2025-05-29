from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    full_name = models.CharField(max_length=255, default=" ", blank=True, null=True)
    user_name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null= True)

    def __str__(self):
        return self.user_name