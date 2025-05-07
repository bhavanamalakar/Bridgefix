from django.db import models

class Employee(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)
    Position=models.CharField(max_length=20)

    def __str__(self):
        return self.First_name