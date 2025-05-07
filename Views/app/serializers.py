from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields='__all__'

    def to_representation(self, instance):
        data= super().to_representation(instance)

        data['fullname']=instance.name +' '+ instance.name

        return data
    
    def validate_phonenum(self,value):
        if len(value) != 10:
            raise serializers.ValidationError("it must contain 10 number")
        return value
    
    def validate(self,data):
        if data['name']==data['email']:
            raise ValueError ("invalide data")
        return data

'''it will not include the summy filed directly if we are using __all__ we need to manually define fields or use to_representation method'''

        # def get_summary(self,obj):
        #     return f"summary of {obj.name}"


    
        
