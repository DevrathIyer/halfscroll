from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    checkpoint = models.FileField(upload_to = 'checkpoints')
    data = models.FileField(upload_to = 'checkpoints/data')
    index = models.FileField(upload_to = 'checkpoints/index')