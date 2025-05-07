from django import forms
from .models import ToDo

class ToDoform(forms.ModelForm):
    
    class Meta:
        model = ToDo
        fields = ["task"]