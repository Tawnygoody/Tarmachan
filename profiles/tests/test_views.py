from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from checkout.models import Order


class TestProfileViews(TestCase):

    def test_user_profile(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_user_profile_not_signed_in(self):
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_user_profile_valid_form(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            '/profile/',
            {
                'default_phone_number': '01234567890',
                'default_street_address1': '123 street',
                'default_street_address2': 'partick',
                'default_town_or_city': 'glasgow',
                'default_county': 'lanarkshire',
                'default_postcode': 'g11 7rr',
                'default_country': 'GB',
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Profile updated successfully!")

    def test_user_profile_invalid_form(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            '/profile/',
            {
                'default_phone_number': '01234567890',
                'default_street_address1': '123 street',
                'default_street_address2': 'partick',
                'default_town_or_city': 'glasgow',
                'default_county': 'lanarkshire',
                'default_postcode': 'g11 7rr',
                'default_country': 'UK',
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Update failed. Please ensure the form is valid")
    
    def test_previous_orders_view(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
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
        response = self.client.get(f'/profile/order_history/{order.order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            f'This is a past confirmation for order {order.order_number}. '
            'A confirmation email was sent on the order date.')
