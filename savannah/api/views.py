from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_orders(request):
    if request.user.is_superuser:
        orders = Order.objects.all()  # Admin can see all orders
    else:
        customer = request.user.customer  # Normal users see only their orders
        orders = Order.objects.filter(customer=customer)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    customer = request.user.customer
    item = request.data.get('item')
    amount = request.data.get('amount')

    order = Order.objects.create(customer=customer, item=item, amount=amount)
    return Response({"message": "Order created", "order_id": order.id})
