from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name='customer-orders'),
    path('orders/create/', views.OrderListCreateView.as_view(), name='create-order'),
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-details'),
    path('orders/<int:order_id>/update/', views.OrderDetailView.as_view(), name='update-order'),
    path('orders/<int:order_id>/delete/', views.OrderDetailView.as_view(), name='delete-order'),
]

# urlpatterns = [
#     path('orders/', views.customer_orders, name='customer-orders'),
#     path('orders/create/', views.create_order, name='create-order'),
#     path('orders/<int:order_id>/', views.order_details, name='order-details'),
#     path('orders/<int:order_id>/update/', views.update_order, name='update-order'),
#     path('orders/<int:order_id>/delete/', views.delete_order, name='delete-order'),

#     path('customers/', views.customers, name='customers'),
#     path('customers/create/', views.create_customer, name='create-customer'),
#     path('customers/<int:customer_id>/', views.customer_details, name='customer-details'),
#     path('customers/<int:customer_id>/update/', views.update_customer, name='update-customer'),
#     path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete-customer'),

# ]