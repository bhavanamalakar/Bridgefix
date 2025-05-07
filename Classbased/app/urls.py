from django.urls import path
from .views import StudentlistView,Studentupdate

urlpatterns = [
    path("post",StudentlistView.as_view(),name='student-list'),
    path("update/<int:pk>",Studentupdate.as_view(),name='student-update')
]
