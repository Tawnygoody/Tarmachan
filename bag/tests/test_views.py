from django.test import TestCase
from django.contrib.messages import get_messages
from products.models import Product, Clearance


class TestBagViews(TestCase):

    def test_view_bag_view(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
