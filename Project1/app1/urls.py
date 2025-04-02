from django.urls import path
from .views import StudentListView,StudentDetailView

urlpatterns = [
    path('student/',StudentListView.as_view()),
    path('student/<int:pk>/',StudentDetailView.as_view()),
]
