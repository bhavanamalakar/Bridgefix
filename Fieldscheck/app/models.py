from django.db import models





class Department(models.Model):
    dep_id=models.IntegerField()
    dep_name=models.CharField(max_length=100)

class Student(models.Model):
    stud_id=models.IntegerField()
    stud_name=models.CharField(max_length=100 ,null=True)
    stud_contact_no=models.CharField(max_length=100,null=False)
    dep_id=models.OneToOneField(Department,on_delete=models.CASCADE,primary_key=True)


'''
null=True: The field is allowed to be NULL in the database (i.e., blank in the database level).

null=False (default): The field must have a value — the database will throw an error if you try to save a record without it.'''


