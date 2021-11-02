from django.test import TestCase
from django.contrib.auth.models import User
from blog.forms import BlogForm


class TestBlogForms(TestCase):
    """Testing Blog views"""

    def test_blog_form(self):
        admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='adminuserpassword',
        )
        self.client.login(username='adminuser', password='adminuserpassword')
        form = BlogForm(
            {
                'title': 'test title',
                'para1': 'test paragraph 1',
                'para4': 'test paragraph 4',
                'para7': 'test paragraph 7',
                'author': admin
            }
        )
        self.assertTrue(form.is_valid())
