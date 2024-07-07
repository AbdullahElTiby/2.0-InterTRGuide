from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default.png')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='defaultpassword')

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggestion = models.TextField(default='Etc.')
    image = models.ImageField(upload_to='category_pics', default='default.png')

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='place_pics', default='default.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')
    def __str__(self):
        return self.name
    
    
class Description(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='descriptions')
    descriptionheader = models.TextField(default='Description')
    text = models.TextField()
    def __str__(self):
        return self.place.name
    


