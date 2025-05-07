from django.db import models

class UserProfile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    image=models.ImageField()
    phonenum=models.CharField(max_length=10)

class Post(models.Model):
    title=models.CharField(max_length=255)
    caption=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

