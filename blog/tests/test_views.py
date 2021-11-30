from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from blog.models import Blog


class TestBlogViews(TestCase):
    """Testing Blog views"""

    def test_all_blogs_view(self):
        """
        Tests the blog page for a 200 status code and that
        the correct template is rendered.
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_detail_view(self):
        """
        Tests the blog detail page for a 200 status code and
        that the blog detail template is rendered.
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        blog = Blog.objects.create(
            title='Test blogpost',
            para1='Test paragraph 1',
            para4='Test paragraph 4',
            para7='Test paragraph 7',
            author=user,
        )
        response = self.client.get(f'/blog/{blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_add_blog_view_superuser(self):
        """
        Tests the add blog page for a 200 status code and that
        the add blog page template is rendered when a superuser
        is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_blog.html')

    def test_add_blog_view_not_superuser(self):
        """
        Tests the add blog page for a 302 status code when a regular
        user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Sorry! Only the team at Tarmachan can access this.')

    def test_edit_blog_view_superuser(self):
        """
        Tests the edit blog page for a 200 status code and that
        the edit blog page template is rendered when a superuser
        is logged in
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        blog = Blog.objects.create(
            title='Test blogpost',
            para1='Test paragraph 1',
            para4='Test paragraph 4',
            para7='Test paragraph 7',
            author=admin,
        )
        response = self.client.get(f'/blog/edit/{blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_blog.html')

    def test_edit_blog_view_not_superuser(self):
        """
        Tests the edit blog page for a 302 status code when a regular
        user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        blog = Blog.objects.create(
            title='Test blogpost',
            para1='Test paragraph 1',
            para4='Test paragraph 4',
            para7='Test paragraph 7',
            author=user,
        )
        response = self.client.get(f'/blog/edit/{blog.id}/')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Sorry! Only the team at Tarmachan can access this.'
        )

    def test_delete_blog_view_superuser(self):
        """
        Tests the delete blog functionality and checks the user
        is redirected back to the blogs page
        """
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        blog = Blog.objects.create(
            title='Test blogpost',
            para1='Test paragraph 1',
            para4='Test paragraph 4',
            para7='Test paragraph 7',
            author=admin,
        )
        response = self.client.get(f'/blog/delete/{blog.id}')
        self.assertRedirects(response, '/blog/')

    def test_delete_blog_view_not_superuser(self):
        """
        Tests the delete blog functionality for a 302 status code
        when a regular user is logged in
        """
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        blog = Blog.objects.create(
            title='Test blogpost',
            para1='Test paragraph 1',
            para4='Test paragraph 4',
            para7='Test paragraph 7',
            author=user,
        )
        response = self.client.get(f'/blog/delete/{blog.id}')
        self.assertEqual(response.status_code, 302)
