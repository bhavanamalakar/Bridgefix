from django.contrib import admin
from .models import Product, Order,Category,blog,OrderItem,Cart

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(blog)
admin.site.register(OrderItem)
admin.site.register(Cart)