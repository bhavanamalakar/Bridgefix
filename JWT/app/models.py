from django.db import models

class instructor(models.model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)

class course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    instructor=models.ForeignKey(instructor,on_delete=models.CASCADE,related_name='course')

class student(models.Model):
    name=models.CharField(max_length=100)
    course=models.ManyToManyField(course)
    
