from django.db import models

class Customer(models.Model):
    customer_id=models.IntegerField()
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    emailid=models.EmailField()
    address=models.TextField()

class Restaurant(models.Model):
    id=models.IntegerField()
    rname=models.CharField(max_length=100)
    emailid=models.EmailField()
    phonenumber=models.CharField(max_length=100)
    address=models.TextField()
    rating=models.IntegerField()

class Rating(models.Model):
    rating_id=models.IntegerField()
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='ratings')
    rest_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    rating=models.IntegerField()

class Menu(models.Model):
    menu_id=models.IntegerField()
    fooditem=models.CharField(max_length=255)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    quntity=models.CharField(max_length=50)

class DeliveryPerson(models.Model):
    d_id=models.IntegerField()
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=200)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)

class Payment(models.Model):
    mode=[
        ('O','Online'),
        ('COD','Cash on Deleviery')
    ]
    transaction_id=models.IntegerField()
    Paymentmode=models.CharField(max_length=2,choices=models.CASCADE)
    amount=models.FloatField()
    totalamount=models.IntegerField()


class Order(models.Model):
    order_id=models.IntegerField()
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders')
    rest_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='orders')
    fooditem=models.CharField(max_length=255)
    fooid=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='orders')
    delivery_id=models.ForeignKey(DeliveryPerson,on_delete=models.CASCADE)
    transaction_id=models.ForeignKey(Payment,on_delete=models.CASCADE)


