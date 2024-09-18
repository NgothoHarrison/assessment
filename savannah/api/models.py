from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link customer to a user
    name = models.CharField(max_length=100)  # Customer's name
    code = models.CharField(max_length=10, unique=True)  # Unique customer code
    phone_number = PhoneNumberField(unique=True)  # Valid phone number field

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  # Link order to a customer
    item = models.CharField(max_length=100)  # Order item name
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Order amount
    time = models.DateTimeField(auto_now_add=True)  # Order creation time

    def __str__(self):
        return f"{self.item} - {self.customer.name}"
