from django.test import TestCase
from django.contrib.auth.models import User
from contact.models import Contact


class TestHomeViews(TestCase):
    """Testing Home Views"""

    def test_home_view(self):
        """
        Tests the home page for a 200 status code and that
        the correct template is rendered.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_us_view(self):
        """
        Tests the about us page for a 200 status code and that
        the correct template is rendered.
        """
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about_us.html')

    def test_product_management_superuser(self):
        """
        Tests the product management page for a 200 status code when
        a superuser is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        response = self.client.get('/product_management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/product_management.html')

    def test_product_management_not_superuser(self):
        """
        Tests the product management page for a 302 status code when
        a regular user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuserpassword',
        )
        self.client.login(username='testuser', password='testuserpassword')
        response = self.client.get('/product_management/')
        self.assertEqual(response.status_code, 302)

    def test_contact_management_superuser(self):
        """
        Tests the contact management page for a 200 status code when
        a superuser user is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        response = self.client.get('/contact_management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_management.html')

    def test_contact_management_not_superuser(self):
        """
        Tests the contact management page for a 302 status code when
        a regular user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuserpassword',
        )
        self.client.login(username='testuser', password='testuserpassword')
        response = self.client.get('/contact_management/')
        self.assertEqual(response.status_code, 302)

    def test_contact_detail_superuser(self):
        """
        Tests the contact detail page for a 200 status code when
        a superuser user is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        contact = Contact.objects.create(
            name='Test Name',
            email='test@email.com',
            subject='Test subject',
            message='Test message',
        )
        response = self.client.get(f'/contact_detail/{contact.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_detail.html')

    def test_contact_detail_not_superuser(self):
        """
        Tests the contact detail page for a 302 status code when
        a regular user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuserpassword',
        )
        self.client.login(username='testuser', password='testuserpassword')
        contact = Contact.objects.create(
            name='Test Name',
            email='test@email.com',
            subject='Test subject',
            message='Test message',
        )
        response = self.client.get(f'/contact_detail/{contact.id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_contact_view_superuser(self):
        """
        Tests the delete contact view and checks the superuser
        is redirected back to the contact management page
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        contact = Contact.objects.create(
            name='Test Name',
            email='test@email.com',
            subject='Test subject',
            message='Test message',
        )
        response = self.client.get(f'/delete_contact/{contact.id}')
        self.assertRedirects(response, '/contact_management/')

    def test_delete_contact_view_not_superuser(self):
        """
        Tests the delete contact view for a 302 status code
        when a regular user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        contact = Contact.objects.create(
            name='Test Name',
            email='test@email.com',
            subject='Test subject',
            message='Test message',
        )
        response = self.client.get(f'/delete_contact/{contact.id}')
        self.assertEqual(response.status_code, 302)
