from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import (
    Product, Clearance, MasterCategory,
    ProductCategory, ProductSubCategory, Comment)


class TestProductViews(TestCase):
    """Testing Products Views"""

    def test_products_view(self):
        """
        Tests for a 200 status code on the products page
        and that the correct template is rendered
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_with_search(self):
        """Tests for product search term"""
        response = self.client.get('/products/', {"q": "test"})
        context = response.context
        self.assertEqual(context['search_term'], 'test')

    def test_products_with_blank_search(self):
        """Tests search functionality with no search term entered"""
        response = self.client.get('/products/', {"q": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "You didn't enter any search criteria!")

    def test_products_with_master_category(self):
        """Tests products with master_category"""
        master_category = MasterCategory.objects.create(
            name="test_master_category"
        )
        response = self.client.get(
            '/products/', {"master_category": "test_master_category"})
        context = response.context
        self.assertTrue(context['current_master_category'])

    def test_products_with_product_category(self):
        """Tests products with product_category"""
        product_category = ProductCategory.objects.create(
            name="test_product_category"
        )
        response = self.client.get(
            '/products/', {"product_category": "test_product_category"})
        context = response.context
        self.assertTrue(context['current_product_category'])

    def test_products_with_product_sub_category(self):
        """Tests products with product_sub_category"""
        product_sub_category = ProductSubCategory.objects.create(
            name="test_product_sub_category"
        )
        response = self.client.get(
            '/products/',
            {"product_sub_category": "test_product_sub_category"})
        context = response.context
        self.assertTrue(context['current_product_sub_category'])

    def test_products_with_clearance_category(self):
        """Tests products in the clearance"""
        clearance = Clearance.objects.create(
            name="test_clearance"
        )
        response = self.client.get(
            '/products/', {"clearance": "test_clearance"})
        context = response.context
        self.assertTrue(context['current_clearance'])

    def test_product_detail(self):
        """
        Tests for a 200 status code on the product detail page
        and that the correct template is rendered
        """
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
            price=49.99,
            clearance=clearance,
            clearance_price=29.99
        )
        comment = Comment.objects.create(
            product=product,
            user=user,
            subject="test subject",
            comment="test comment",
            rating=3
        )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_if_superuser(self):
        """Tests the add product view for a 200 status code"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_if_superuser_post(self):
        """Tests the add product form if the user is a superuser"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
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
        form_data = {
                'name': 'test product',
                'description1': 'test description',
                'price': 45.99,
                'clearance': 1,
                'master_category': 1,
                'product_category': 1,
                'product_sub_category': 1,
            }
        response = self.client.post(
            '/products/add/', form_data
        )
        product = Product.objects.get(name='test product')
        self.assertRedirects(response, f'/products/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Successfully added product!"
        )

    def test_add_product_if_superuser_post_invalid(self):
        """tests posting an invalid product form"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
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
        form_data = {
                'name': 'test product',
                'description1': 'test description',
                'price': '',
                'clearance': 1,
                'master_category': 1,
                'product_category': 1,
                'product_sub_category': 1,
            }
        response = self.client.post(
            '/products/add/', form_data
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Failed to add product. Please ensure the form is valid."
        )

    def test_add_product_not_superuser(self):
        """
        Tests the add product page for a 302 status code when a regular
        user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Sorry! Only the team at Tarmachan can access this.'
        )

    def test_edit_product_if_superuser(self):
        """
        Tests the edit product view for a 200 status code
        if a superuser is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance
        )
        response = self.client.get(f'/products/edit/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_if_superuser_post(self):
        """Tests posting the edit product form when form is valid"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
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
        )
        response = self.client.post(
            f'/products/edit/{product.id}',
            {
                'name': 'test product edit',
                'description1': 'test description',
                'price': '29.99',
                'clearance': 1,
                'master_category': 1,
                'product_category': 1,
                'product_sub_category': 1,
            }
        )
        edit_product = Product.objects.get(name='test product edit')
        self.assertEqual(edit_product.name, 'test product edit')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Successfully updated product!"
        )

    def test_edit_product_if_superuser_post_invalid(self):
        """Tests submitting the edit product form when it is invalid"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
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
        )
        response = self.client.post(
            f'/products/edit/{product.id}',
            {
                'name': '',
                'description1': 'test description',
                'price': '',
                'clearance': 1,
                'master_category': 1,
                'product_category': 1,
                'product_sub_category': 1,
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Failed to update product. Please ensure the form is valid."
        )

    def test_edit_product_not_superuser(self):
        """Tests regular users trying to access the edit product form"""
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
            clearance=clearance
        )
        response = self.client.get(f'/products/edit/{product.id}')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Sorry! Only the team at Tarmachan can access this.'
        )

    def test_delete_product_superuser(self):
        """Tests superuser deleting a product"""
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance
        )
        response = self.client.get(f'/products/delete/{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertRedirects(response, '/products/')
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Product deleted!")

    def test_delete_product_not_superuser(self):
        """Tests the response of regular users, trying to delete a product"""
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
            clearance=clearance
        )
        response = self.client.get(f'/products/delete/{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertRedirects(response, '/')
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Sorry! Only the team at Tarmachan can access this.")

    def test_add_comment(self):
        """Tests a logged in user adding a comment"""
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
            clearance=clearance
        )
        response = self.client.post(f'/products/add_comment/{product.id}', {
            'product': 'test product',
            'user': 'testuser',
            'subject': 'test subject',
            'comment': 'test message',
            'rating': 3,
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Successfully added comment!'
        )

    def test_delete_comment_with_additional_comments(self):
        """Tests a user deleting their own comment"""
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
            clearance=clearance
        )
        comment = Comment.objects.create(
            product=product,
            user=user,
            subject="test subject",
            comment="test comment",
            rating=3
        )
        second_comment = Comment.objects.create(
            product=product,
            user=user,
            subject="test subject 2",
            comment="test comment 2",
            rating=2
        )
        response = self.client.get(f'/products/delete_comment/{comment.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Review test subject has been deleted!'
        )

    def test_delete_comment(self):
        """Tests a user deleting their own comment"""
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
            clearance=clearance
        )
        comment = Comment.objects.create(
            product=product,
            user=user,
            subject="test subject",
            comment="test comment",
            rating=3
        )
        response = self.client.get(f'/products/delete_comment/{comment.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Review test subject has been deleted!'
        )

    def test_delete_comment_not_reviewer(self):
        """Tests a non-reviewer from deleting a comment"""
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@gmail.com',
            password='testpassword2'
        )
        clearance = Clearance.objects.create(
            name='test clearance'
        )
        product = Product.objects.create(
            name="test product",
            description1="test description",
            price="49.99",
            clearance=clearance
        )
        comment = Comment.objects.create(
            product=product,
            user=user2,
            subject="test subject",
            comment="test comment",
            rating=3
        )
        response = self.client.get(f'/products/delete_comment/{comment.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Only the team at Tarmachan and the reviewer can access this.'
        )
