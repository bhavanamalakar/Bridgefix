from django.urls import path
from . import views

urlpatterns = [
    path('',views.item_list,name='list_user'),
    path('detail/',views.item_detail,name='datail-user'),
    # path('update/<int:pk>/',views.user_update,name='update-user'),
    # path('delete/<int:pk>/',views.user_delete,name='delete-user'),
]