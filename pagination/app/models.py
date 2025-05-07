from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


class Product(models.Model):
    name=models.CharField(max_length=255)
    discription=models.TextField()
    price=models.IntegerField()
    created_at=models.DateField()