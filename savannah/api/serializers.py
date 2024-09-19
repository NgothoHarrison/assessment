from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']
        read_only_fields = ['customer'] # Customer should not be updated directly, only through the customer endpoint
