# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from .models import Order
# from .serializers import OrderSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def customer_orders(request):
#     if request.user.is_superuser:
#         orders = Order.objects.all()  # Admin can see all orders
#     else:
#         customer = request.user.customer  # Normal users see only their orders
#         orders = Order.objects.filter(customer=customer)

#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_order(request):
#     customer = request.user.customer
#     item = request.data.get('item')
#     amount = request.data.get('amount')

#     order = Order.objects.create(customer=customer, item=item, amount=amount)
#     return Response({"message": "Order created", "order_id": order.id})

# from django.shortcuts import render, get_object_or_404, redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Order
# from .serializers import OrderSerializer
# from rest_framework import status
# from django.contrib.auth.decorators import login_required


# # View customer's orders
# @login_required
# @api_view(['GET'])
# def customer_orders(request):
#     if request.user.is_superuser:
#         orders = Order.objects.all()
#     else:
#         orders = Order.objects.filter(customer=request.user)
    
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


# # Create a new order
# @login_required
# @api_view(['POST'])
# def create_order(request):
#     serializer = OrderSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save(customer=request.user)  # Associate the order with the logged-in user
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # View order details
# @login_required
# @api_view(['GET'])
# def order_details(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
    
#     if request.user.is_superuser or order.customer == request.user:
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
#     else:
#         return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


# # Update an order
# @login_required
# @api_view(['PUT'])
# def update_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
    
#     if request.user.is_superuser or order.customer == request.user:
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


# # Delete an order
# @login_required
# @api_view(['DELETE'])
# def delete_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
    
#     if request.user.is_superuser or order.customer == request.user:
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Order
from .serializers import OrderSerializer
from openId.models import Customer

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # If the user is a superuser, return all orders
        if self.request.user.is_superuser:
            return Order.objects.all()
        # Otherwise, return orders associated with the authenticated user
        try:
            customer = Customer.objects.get(user=self.request.user)
            return Order.objects.filter(customer=customer)
        except Customer.DoesNotExist:
            return Order.objects.none()  # If the customer does not exist, return no orders

    def perform_create(self, serializer):
        # Set the customer field automatically when creating an order
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = generics.get_object_or_404(Order, pk=self.kwargs['order_id'])
        # If the user is not a superuser, ensure they only access their own orders
        if not self.request.user.is_superuser:
            customer = Customer.objects.get(user=self.request.user)
            if obj.customer != customer:
                raise permissions.PermissionDenied("You do not have permission to access this order.")
        return obj

