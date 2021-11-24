from django.test import TestCase
from profiles.forms import UserProfileForm


class TestCheckoutForms(TestCase):
    """Testing Checkout forms"""

    def test_order_form(self):
        form = UserProfileForm(
            {
                'default_phone_number': '01234567890',
                'default_street_address1': '123 street',
                'default_street_address2': 'partick',
                'default_town_or_city': 'glasgow',
                'default_county': 'lanarkshire',
                'default_postcode': 'g11 7rr',
                'default_country': 'GB',
            }
        )
        self.assertTrue(form.is_valid())
