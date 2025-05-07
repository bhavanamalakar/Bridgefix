from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):


    class Meta:
        model=Student
        fields=['id','name','email','is_active','created_at']



    def to_representation(self,instance):
        data=super().to_representation(instance)

        if not instance.is_active:
            data.pop('email')

        data['is_active']="Active" if instance.is_active else "Inactive"

        return data
    
    # def to_representation(self,instance):
    #     data=super().to_representation(instance)
    #     data['created_at']=instance.created_at.strftime('%y-%m-%d')
    #     return data
    
    # def to_internal_value(self, data):

    #     data=super().to_internal_value(data)
    #     if 'name' in data:

    #         data['name']=data['name'].upper()
    #     return data
    def to_representation(self, instance):

        data=super().to_representation(instance)
        if instance.name:

            data['name']=data['name'].upper()
        return data   


































# EXAMPLES:
'''
Scenario to_representation()
Format date fields	Convert created_at to YYYY-MM-DD

Modify how names are displayed	Show full name as first_name + last_name

Hide certain fields	Remove password from the response

Add computed fields	Add a full_name field from first_name & last_name

Change field representation	Show is_active as "Active"/"Inactive" instead of True/False

'''
# to_internal_value(): Use this when you want to modify or validate incoming data before saving it.

'''
Scenario	Example
Standardize input formats	Convert username to lowercase

Clean data before saving	Trim spaces from phone numbers

Enforce specific formats	Ensure email is always stored in lowercase

Validate custom input fields	Reject non-numeric phone numbers

Prevent invalid data	Raise an error if age is negative
'''



