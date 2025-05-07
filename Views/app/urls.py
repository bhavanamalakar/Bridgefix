from django.urls import path,include
from .views import UserProfileViewset
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import SimpleRouter

router=DefaultRouter()
# router=SimpleRouter()
router.register(r'user',UserProfileViewset,basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

