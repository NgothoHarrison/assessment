from django.urls import path, include
from .views import *
urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('customers/', CustomerListCreateView.as_view(), name='customer'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:pk>/update/', CustomerDetailView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDetailView.as_view(), name='customer-delete'),


]