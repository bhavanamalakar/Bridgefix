from django.db import models
from django.contrib.auth.models import AbstractUser

    
class Role(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Permission(models.Model):
    name=models.CharField(max_length=100,unique=True)
    code_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    permission=models.ForeignKey(Permission,on_delete=models.CASCADE)


class User(AbstractUser):
    role=models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.username}"

