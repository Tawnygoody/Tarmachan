from django.test import TestCase


class TestBagViews(TestCase):
    """Testing Bag Views"""
    def test_view_bag_view(self):
        """Testing the view_bag view"""
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
