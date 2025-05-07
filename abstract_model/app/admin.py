from django.contrib import admin

from .models import Student,Teacher,Baseclass

admin.site.register(Student)

admin.site.register(Teacher)
# admin.site.register(Baseclass) #  it will give error
