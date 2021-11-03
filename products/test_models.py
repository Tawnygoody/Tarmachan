from django.test import TestCase
from products.models import Product, Clearance, MasterCategory, ProductCategory, ProductSubCategory, Comment
from django.contrib.auth.models import User


class TestProductModels(TestCase):
    """Testing Contact models"""

    def test_master_category_model(self):
        master_category = MasterCategory.objects.create(
            name='test_master_category',
            friendly_name='Test Master Category'
        )
        self.assertEqual(str(master_category), master_category.name)

    def test_product_category_model(self):
        product_category = ProductCategory.objects.create(
            name='test_product_category',
            friendly_name='Test Product Category'
        )
        self.assertEqual(str(product_category), product_category.name)

    def test_product_sub_category_model(self):
        product_sub_category = ProductSubCategory.objects.create(
            name='test_product_sub_category',
            friendly_name='Test Product Sub Category'
        )
        self.assertEqual(str(product_sub_category), product_sub_category.name)

    def test_clearance_model(self):
        clearance = Clearance.objects.create(
            name='clearance',
            friendly_name='Clearance'
        )
        self.assertEqual(str(clearance), clearance.name)

    def test_product_model(self):
        clearance = Clearance.objects.create(
            name='clearance',
            friendly_name='Clearance'
        )
        master_category = MasterCategory.objects.create(
            name='test_master_category',
            friendly_name='Test Master Category'
        )
        product_category = ProductCategory.objects.create(
            name='test_product_category',
            friendly_name='Test Product Category'
        )
        product_sub_category = ProductSubCategory.objects.create(
            name='test_product_sub_category',
            friendly_name='Test Product Sub Category'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price=49.99,
            clearance=clearance,
            master_category=master_category,
            product_category=product_category,
            product_sub_category=product_sub_category,
        )
        self.assertEqual(str(product), product.name)

    def test_comment_model(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        clearance = Clearance.objects.create(
            name='clearance',
            friendly_name='Clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price=49.99,
            clearance=clearance
        )
        comment = Comment.objects.create(
            product=product,
            user=user,
            subject="test subject",
            comment="test comment",
            rating=3,
        )
        self.assertEqual(str(comment), comment.subject)
