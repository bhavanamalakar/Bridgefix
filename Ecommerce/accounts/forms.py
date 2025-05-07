from django import forms
from .models import User, Role

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="Select Role")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

