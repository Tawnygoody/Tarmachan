from django.test import TestCase
from contact.models import Contact, NewsletterSubscription


class TestContactModels(TestCase):
    """Testing Contact models"""

    def test_contact_model(self):
        contact = Contact.objects.create(
            name="test name",
            email="test@email.com",
            subject="test subject",
            message="test message",
        )
        self.assertEqual(str(contact), contact.subject)

    def test_newsletter_model(self):
        subscriber = NewsletterSubscription.objects.create(
            email="test@email.com"
        )
        self.assertEqual(str(subscriber), subscriber.email)
