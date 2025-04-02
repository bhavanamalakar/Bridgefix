from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import OTPModel
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email):
    otp_record, created = OTPModel.objects.get_or_create(email=email)

    if not created and otp_record.is_valid():
        otp = otp_record.otp 
    else:
        otp = generate_otp()
        otp_record.otp = otp
        otp_record.created_at = now()
        otp_record.save()

    send_mail(
        "Your OTP Code",
        f"Your OTP code is {otp}",
        "your_email@gmail.com",
        [email],
        fail_silently=False,
    )
    return otp

def request_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        send_otp_email(email)
        return redirect("verify_otp")  
    return render(request, "request_otp.html")

def verify_otp(request):
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        otp = request.POST.get("otp")

        try:
            otp_record = OTPModel.objects.get(email=email)
            if otp_record.otp == otp and otp_record.is_valid():
                message = "OTP Verified Successfully!"
            else:
                message = "Invalid or Expired OTP!"
        except OTPModel.DoesNotExist:
            message = "No OTP found for this email!"

    return render(request, "verify_otp.html", {"message": message})
