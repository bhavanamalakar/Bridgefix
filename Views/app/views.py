from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle


class UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class= UserProfileSerializer
    throttle_classes=[UserRateThrottle,AnonRateThrottle]

#filter based api request
    def get_queryset(self):
        queryset= super().get_queryset()
        name=self.request.query_params.get('name',None)
        if name:
            queryset=queryset.filter(name__icontains=name)
        return queryset
        

