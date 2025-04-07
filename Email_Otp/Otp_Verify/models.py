from django.db import models
from django.utils.timezone import now

class OTPModel(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        
        return (now() - self.created_at).seconds <= 300  # 300 seconds = 5 minutes

    def __str__(self):
        return f"{self.email} - {self.otp}"
    





