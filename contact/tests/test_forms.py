from django.test import TestCase
from contact.forms import (
    ContactForm, NewsletterUnsubscribeForm, NewsletterForm)


class TestContactForms(TestCase):
    """Testing Contact forms"""

    def test_contact_form(self):
        form = ContactForm(
            {
                'name': 'test name',
                'email': 'test@email.com',
                'subject': 'test subject',
                'message': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_newsletterform(self):
        form = NewsletterForm(
            {
                'email': 'test@email.com'
            }
        )
        self.assertTrue(form.is_valid())
