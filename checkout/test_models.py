from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from products.models import Product, Clearance


class TestOrderModels(TestCase):
    """Testing Blog models"""

    def test_order_model(self):
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
        self.assertEqual(str(order), order.order_number)

    def test_order_line_item_model(self):
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
        clearance = Clearance.objects.create(
            name='test_clearance'
        )
        product = Product.objects.create(
            sku='12345',
            name="Test product",
            description1="test description",
            price=49.99,
            clearance=clearance
        )
        order_line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            lineitem_total=49.99
        )

        self.assertEqual(
            str(order_line_item),
            f'SKU {order_line_item.product.sku} on order {order.order_number}'
        )
