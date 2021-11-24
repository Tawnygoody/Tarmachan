from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog


class TestBlogModels(TestCase):
    """Testing Blog models"""

    def test_blog_model(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        blog = Blog.objects.create(
            title="test blog",
            para1="test paragraph 1",
            para4="test paragraph 4",
            para7="test paragraph 7",
            author=user
        )
        self.assertEqual(str(blog), blog.title)
