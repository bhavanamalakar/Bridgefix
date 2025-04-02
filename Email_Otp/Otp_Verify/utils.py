from django.core.mail import send_mail
from django.utils.timezone import now
from .models import OTPModel

def send_otp(email):
    """Generate or reuse an OTP and send it via email."""
    otp_entry, created = OTPModel.objects.get_or_create(email=email)

    if not created and otp_entry.is_valid():
        otp = otp_entry.otp  # Use existing OTP if valid
    else:
        otp = OTPModel.generate_otp()
        otp_entry.otp = otp
        otp_entry.created_at = now()
        otp_entry.save()

    # Send OTP via email
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}. It is valid for 5 minutes.'
    send_mail(subject, message, 'your_email@gmail.com', [email])

    return otp  # Return for debugging/testing
