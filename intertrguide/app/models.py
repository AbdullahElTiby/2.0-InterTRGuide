from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default.png')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='defaultpassword')

    def __str__(self):
        return self.username
