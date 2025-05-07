from rest_framework import viewsets
from .models import Book, Publisher
from .serializers import BookModelSerializer,PublisherModelSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset=Publisher.objects.all()
    serializer_class=PublisherModelSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookModelSerializer