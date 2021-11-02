from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Product, Clearance


class TestWishlistViews(TestCase):

    def test_wishlist_view_not_signed_in(self):
        response = self.client.get("/wishlist/")
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Sorry! Only members can access the wishlist")

    def test_wishlist_view_signed_in(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get("/wishlist/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist/wishlist.html")

    def test_add_to_wishlist_not_signed_in(self):
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance,
        )
        response = self.client.get(f'/wishlist/add_to_wishlist/{product.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Sorry! Only members can add products to their wishlist")

    def test_add_to_wishlist(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance,
        )
        response = self.client.get(f'/wishlist/add_to_wishlist/{product.id}')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "test product has been added to your wishlist")

    def test_remove_from_wishlist(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance,
        )
        product.user_wishlist.add(user)
        response = self.client.get(f'/wishlist/add_to_wishlist/{product.id}')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "test product has been removed from your wishlist")
