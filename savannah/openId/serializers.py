from rest_framework import serializers
from .models import Customer
from django.core.validators import RegexValidator

class CustomerSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
            )
        ]
    )
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'code', 'phone_number']
        read_only_fields = ['user']  # The user will be set automatically

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number']  # You can include other fields that were not filled initially
