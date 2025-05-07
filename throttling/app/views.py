from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle

# class UserProfileViewset(viewsets.ModelViewSet):
    # queryset=UserProfile.objects.all()
    # serializer_class= UserProfileSerializer
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    


# use of scopedrate:A scope is a string that identifies a specific group of API endpoints or a particular user role or context. 

# class UserProfileViewset(viewsets.ModelViewSet):
#     queryset=UserProfile.objects.all()
#     serializer_class= UserProfileSerializer
#     throttle_classes=[ScopedRateThrottle]
#     throttle_scope='custom_scope' 

# custome throthling

class UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class= UserProfileSerializer
    # throttle_classes=['app.custom_throttles.Basecustom']
    