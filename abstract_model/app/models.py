from django.db import models

class Baseclass(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract=True

'''this baseclass is our abstract class we have added common field in it and then inherite it with another classes. if we don't want any of field
in any model so we define that particulare field None.'''

class Student(Baseclass):
    fees=models.FloatField()
    join_Date=None

class Teacher(Baseclass):
    salary=models.IntegerField()
    join_Date=models.DateField(auto_now_add=True)

# MAKING CUSTOM USER

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):

    def create_user(self,email,password=None,**extrafield):

        if not email:
            raise ValueError("email is required")
        email=self.normalize_email(email)
        user=self.model(email=email,**extrafield)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password,**extrafiled):

        extrafiled.setdefault('is_staff',True)
        extrafiled.setdefault('is_superuser',True)

        return self.create_superuser(email,password,**extrafiled)
    
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address',max_length=255,unique=True)
    DOB=models.DateField()
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=MyUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['DBO']
