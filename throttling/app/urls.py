from django.urls import path,include
from .views import UserProfileViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'user',UserProfileViewset)

urlpatterns = [
    path("",include(router.urls)),
]
