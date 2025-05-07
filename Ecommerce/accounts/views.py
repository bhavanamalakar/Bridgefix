from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Role
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            user.role.add(form.cleaned_data['role']) 
            messages.success(request, "Registration successful. Please login.")
            return redirect('login_view')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login_view')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def dashboard_view(request):
    roles = request.user.role.values_list('name', flat=True)
    return render(request, 'dashboard.html', {'roles': roles})
