from rest_framework import viewsets
from .models import Post,Order
from .serializers import PostSerializer,OrderSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer