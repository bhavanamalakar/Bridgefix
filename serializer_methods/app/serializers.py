from rest_framework import serializers
from .models import Post,Order,Product

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

    def to_representation(self, instance):
        rep=super().to_representation(instance)
        # formate data
        rep['created_at']=instance.created_at.strftime('%d-%m-%y')
        # show author's username
        rep['author']=instance.author.username
        # Add custom summary field
        rep['summary']=instance.content[:30] +'...' if len(instance.content)>30 else instance.content
        return rep

'''
This is simle wasy of using to representation
1. Field formating
2. Custome field creation
3. Related object conversion '''

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Replace product ID with product details
        rep['product'] = {
            'name': instance.product.name,
            'price': float(instance.product.price)
        }
        # Add seller username
        rep['seller'] = instance.product.seller.username
        # Show buyer username
        rep['buyer'] = instance.buyer.username
        # Format ordered_at
        rep['ordered_at'] = instance.ordered_at.strftime('%d-%m-%Y')
        # Add total price
        rep['total_price'] = float(instance.product.price * instance.quantity)
        return rep


# to_internal_value()::converting incoming json to model compatible data

    # This is fine if you are handling all fields manually
    def to_internal_value(self, data):
        update_data_field={
            'product':data.get('product'),
            'buyer':data.get('buyer'),
            'quantity': data.get('quantity')
        }
    
        return super().to_internal_value(update_data_field)


# SUPER() USES
# You want to keep default behavior | Use super() |
# without using super : like if you are completely customizing fields yourself | No need for super() 
