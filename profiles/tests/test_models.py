from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestProfileModels(TestCase):
    """Testing Profile models"""

    def test_user_profile_model(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        user_profile = UserProfile.objects.get(
            user=user
        )
        self.assertEqual(str(user_profile), user_profile.user.username)
