from django.db import models

class Book(models.Model):
    # textfields
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description=models.TextField(blank=True)

    # numeric fields
    stock=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    # booleanfield
    is_actice=models.BooleanField(default=True)

    # date time field
    event_date = models.DateField()
    event_time = models.TimeField()
    created_at=models.DateField( auto_now_add=False)  # Updates timestamp on every save.
    updated_at=models.DateTimeField(auto_now=False)       # Sets timestamp only on creation.

    # file/image upload
    profile_pic=models.ImageField(upload_to='profiles/',blank=True)
    resume=models.FileField(upload_to='resume/',blank=True)

    # json data upload
    settings=models.JSONField(default=dict)

# relational fields

class author(models.Model):
    name=models.CharField(max_length=10)

class kitab(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    
















    def __str__(self):
        return self.title

