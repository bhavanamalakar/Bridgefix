from django.urls import path,include
from .views import PostViewset,OrderViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'post',PostViewset)
router.register(r'order',OrderViewset)

urlpatterns = [
    path('',include(router.urls)),
]
