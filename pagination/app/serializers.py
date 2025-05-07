from rest_framework import serializers
from .models import Book,Product


class BookSerializer(serializers.ModelSerializer):
    total_price=serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'