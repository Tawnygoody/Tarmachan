from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Product, Clearance
from checkout.models import Order


class TestCheckoutViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.checkout = reverse('checkout')
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.clearance = Clearance.objects.create(
            name='test clearance'
        )
        self.product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=self.clearance
        )
        self.add_to_bag = reverse(
            "add_to_bag",
            kwargs={"item_id": self.product.id})


    def test_checkout_view_empty_bag(self):
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "There's nothing in your bag at the moment")

    def test_checkout_view_with_bag(self):
        self.client.post(
            self.add_to_bag,
            data={"quantity": "2", "redirect_url": "/"}
        )
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_success(self):
        order = Order.objects.create(
            full_name="Test Order",
            email="test@email.com",
            phone_number="0123456789",
            street_address1="123 Street",
            town_or_city="Test Town",
            country="UK",
            delivery_cost=0.00,
            order_total=60,
            grand_total=60,
            stripe_pid="1234567890",
        )
        order.save()
        response = self.client.get(
            f"/checkout/checkout_success/{order.order_number}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
