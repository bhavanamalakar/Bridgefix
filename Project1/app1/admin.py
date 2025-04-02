from django.contrib import admin


from .models import Student

class studentadmin(admin.ModelAdmin):

    data=('name','email','is_active')

admin.site.register(Student,studentadmin)