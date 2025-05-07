from django.urls import path
from .views import BookListView

urlpatterns = [
    path("",BookListView.as_view(),name='listbook'),
    # path("update/<int:pk>",BookDetailView.as_view(),name='bookdetail')
]
