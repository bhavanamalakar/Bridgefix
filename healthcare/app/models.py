from django.db import models

class Patient(models.Model):
    gender=[
        ('F','Female'),
        ('M','Male'),
        ('O','Other'),
    ]
    Patient_id=models.IntegerField()
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Dob=models.DateField("DateOfBirth")
    Gender=models.CharField(max_length=1,choices=gender)
    Address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.First_name

class Doctor(models.Model):
    Doctor_id=models.IntegerField()
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    specilization=models.CharField(max_length=100)
    scheduleDate=models.DateTimeField()

class Appointment(models.Model):
    status={
        's':'shedualed',
        'c':'canceled',
    }
    App_id=models.IntegerField()
    app_Date=models.DateField()
    Patient_id=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Dr_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    app_status=models.CharField(max_length=1,choices=status)

class Billing(models.Model):
    status={
        'D':'Due',
        'P':'Paid',
    }
    Bill_id=models.IntegerField()
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Bill_status=models.CharField(max_length=1,choices=status)
    Date=models.DateTimeField()
    amount=models.FloatField()

