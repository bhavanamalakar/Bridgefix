from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('cart/',views.cart,name='cart'),
    path('add_cart/<int:pk>/',views.add_cart,name='add_cart'),
    path('increase_quantity/<int:pk>/',views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/<int:pk>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove/<int:item_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('place_order/<int:pk>/', views.place_order, name='place_order'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('order_success/', views.order_success, name='order_success'),
]
