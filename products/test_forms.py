from django.test import TestCase
from products.forms import ProductForm, CommentForm
from django.contrib.auth.models import User
from products.models import Product, Clearance, MasterCategory, ProductCategory, ProductSubCategory


class TestProductForms(TestCase):
    """Testing Product forms"""

    def test_product_form(self):
        clearance = Clearance.objects.create(
            name='test_clearance'
        )
        master_category = MasterCategory.objects.create(
            name='test_master_category'
        )
        product_category = ProductCategory.objects.create(
            name='test_product_category'
        )
        product_sub_category = ProductSubCategory.objects.create(
            name='test_product_sub_category'
        )
        form = ProductForm(
            {
                'name': 'test product',
                'description1': 'test description',
                'price': 45.99,
                'clearance': clearance,
                'master_category': master_category,
                'product_category': product_category,
                'product_sub_category': product_sub_category,
            }
        )
        self.assertTrue(form.is_valid())

    def test_comment_form(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        clearance = Clearance.objects.create(
            name='test_clearance'
        )
        master_category = MasterCategory.objects.create(
            name='test_master_category'
        )
        product_category = ProductCategory.objects.create(
            name='test_product_category'
        )
        product_sub_category = ProductSubCategory.objects.create(
            name='test_product_sub_category'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance,
            master_category=master_category,
            product_category=product_category,
            product_sub_category=product_sub_category,
        )
        form = CommentForm(
            {
                'product': product,
                'user': user,
                'subject': '',
                'comment': '',
                'rating': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')
        self.assertEqual(form.errors['comment'][0], 'This field is required.')
        self.assertEqual(form.errors['rating'][0], 'This field is required.')
