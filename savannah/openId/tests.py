from django.test import TestCase
from .models import Customer
from django.contrib.auth.models import User

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.customer = Customer.objects.create(user=self.user, name='John Doe', code='CUST007', phone_number='+1234567890')

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.code, 'CUST007')
        self.assertEqual(self.customer.phone_number, '+1234567890')

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'John Doe')
