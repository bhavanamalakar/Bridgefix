from rest_framework import serializers
from .models import Book,Publisher

# Nested serializer

class PublisherModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()                       #custome field added
    class Meta:
        model=Publisher
        fields=['name','password','confirm_password','title']

    '''SerializerMethodField:
When the field is not a direct model field.
When the value needs to be calculated dynamically.
To transform the field (e.g., formatting, conditional values).'''

    def get_title(self,object):
        return f"this is {object.name}"


    #filed level validation
    def validate_name(self,value):
        if 'admin' in value:
            raise serializers.ValidationError("user can not contain admin")
        return value
    
    #objectlevel validation : if we want to validate more then one field
    def validate(self,data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("password does not match")
        return data
        

class BookModelSerializer(serializers.ModelSerializer):
    publisher=PublisherModelSerializer()

    class Meta:
        model=Book
        fields=['title','author','published_date','price','publisher']



# using simple serializer 
# class BookSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     author=serializers.CharField(max_length=100)
#     published_date=serializers.DateField()
#     price=serializers.DecimalField(max_digits=6,decimal_places=2)
#     password=serializers.CharField(write_only=True)
#     confirm_password=serializers.CharField(write_only=True)


# # using Modelserializer
# class BookModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Book
#         fields=['title','author','published_date','price']


# Customizing serializer fields
'''Sometimes you may want to customize how a serializer field is displayed or behave. This can be done by overriding field definitions in the serializer class.'''
# class BookModelSerializer(serializers.ModelSerializer):
#     publisher_name=serializers.CharField(source='publisher.name',read_only=True)

#     class Meta:
#         model=Book
#         fields=['title','author','published_date','price']




