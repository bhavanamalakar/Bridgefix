from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,PublisherViewSet

router=DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'publisher',PublisherViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
