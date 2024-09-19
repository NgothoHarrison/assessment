# it will be triggered when a user is created
# and a customer profile will be created for the user
# with the same username as the user and a unique code

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        # Generate a unique code for the customer (for example, based on their user ID)
        code = f'CUST{instance.id:04d}'
        Customer.objects.create(user=instance, name=instance.username, code=code)

