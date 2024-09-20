from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name='customer-orders'),
    path('orders/create/', views.OrderListCreateView.as_view(), name='create-order'),
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-details'),
    path('orders/<int:order_id>/update/', views.OrderDetailView.as_view(), name='update-order'),
    path('orders/<int:order_id>/delete/', views.OrderDetailView.as_view(), name='delete-order'),
]
