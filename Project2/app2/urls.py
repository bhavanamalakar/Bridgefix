from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/<int:book_id>/', book_detail, name='book-detail'),
]
