from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.customer_orders, name='customer-orders'),
    path('orders/create/', views.create_order, name='create-order'),
]