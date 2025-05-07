from django.db import models

class UserProfile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    image=models.ImageField()
    phonenum=models.CharField(max_length=10)
    