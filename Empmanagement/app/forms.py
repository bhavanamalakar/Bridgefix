from django import forms
from .models import Employee

class Empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['First_name','Last_name','Email','Phone_number','Dept','Position']