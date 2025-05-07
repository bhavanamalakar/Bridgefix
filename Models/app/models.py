from django.db import models


class Department(models.Model):
    dep_id=models.IntegerField()
    dep_name=models.CharField(max_length=100)

class Student(models.Model):
    stud_id=models.IntegerField(primary_key=True)
    stud_name=models.CharField(max_length=100)
    stud_contact_no=models.IntegerField()
    dep_id=models.OneToOneField(Department,on_delete=models.CASCADE)
    
# ONETOONE relationship-

# class UID(models.Model):
#     reg_no=models.IntegerField()
#     roll_no=models.IntegerField()

# class Student(models.Model):
#     UID=models.OneToOneField(UID,on_delete=models.CASCADE)
#     name=models.CharField(max_length=200)
#     contact=models.IntegerField()

# MANYTOMANY relationship

class product(models.Model):
    prod_id=models.IntegerField()
    prod_name=models.CharField(max_length=100)

class customer (models.Model):
    cust_id=models.IntegerField()
    cust_name=models.CharField(max_length=100)
    prod=models.ManyToManyField(product)

# So a product can have multiple customers whereas a customer can have multiple products. In the above code.

# ManytoOne relationship


class Album(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)

class Song(models.Model):
    title=models.CharField(max_length=100)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    