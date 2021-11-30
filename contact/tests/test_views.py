from django.test import TestCase
from django.contrib.messages import get_messages
from contact.models import NewsletterSubscription, Contact


class TestContactViews(TestCase):
    """Testing Contact Views"""

    def test_contact_view_get(self):
        """
        Tests the contact page for a 200 status code and that
        the correct template is rendered.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_view_post(self):
        """
        Tests when the contact form is valid, returns a 200 status
        code, checks the correct message is displayed and the
        contact objects length is 1.
        """
        response = self.client.post('/contact/', {
            'name': 'testuser',
            'email': 'testuser@email.com',
            'subject': 'test subject',
            'message': 'test message'
        })
        self.assertEqual(response.status_code, 200)
        existing_contacts = Contact.objects.all()
        self.assertEqual(len(existing_contacts), 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Thanks testuser! test subject has been sent to the \
                    Tarmachan team.')

    def test_contact_view_post_error(self):
        """
        Test when the contact form is invalid that the correct
        message is being rendered.
        """
        response = self.client.post('/contact/', {
            'name': 'testuser',
            'email': 'testuser@email.com',
            'subject': '',
            'message': ''
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Failed to send message, please ensure all fields are correct')

    def test_newsletter_subscriber_post(self):
        """
        Tests when the newsletter subscription form is submitted
        the existing_subscribers is equal to 1, and the correct
        message is rendered
        """
        response = self.client.post('/contact/newsletter_register/', {
            'email': 'testuser@email.com'
        })
        existing_subscribers = NewsletterSubscription.objects.all()
        self.assertEqual(len(existing_subscribers), 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'You are now subscribed to the Tarmachan newsletter. \
                        We have sent an email confirmation to you.')

    def test_newsletter_subscriber_post_error(self):
        """
        Tests when the newsletter subscription form is invalid the
        correct message is rendered
        """
        response = self.client.post('/contact/newsletter_register/', {
            'email': ''
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Failed to subscribe. Please ensure the email you've entered is \
                    valid")

    def test_newsletter_already_subscribed_post(self):
        """
        Tests when an already subscribed member tries to subscribe
        again, and ensure the correct message is rendered.
        """
        subscriber = NewsletterSubscription.objects.create(
            email='testuser@email.com'
        )
        response = self.client.post('/contact/newsletter_register/', {
            'email': "testuser@email.com"
        })
        existing_subscribers = NewsletterSubscription.objects.all()
        self.assertEqual(len(existing_subscribers), 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'This email address is already subscribed to the Tarmachan \
                        newsletter.')

    def test_unsubscribe_view_get(self):
        """
        Tests the unsubscribe page for a 200 status code and that
        the correct template is rendered.
        """
        response = self.client.get('/contact/newsletter_unsubscribe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'contact/newsletter_unsubscribe.html'
        )

    def test_newsletter_unsubscribe_post(self):
        """
        Tests the unsubscribe page and ensures that existing_subscribers
        length is = 0 once the user has unsubscribed
        """
        subscriber = NewsletterSubscription.objects.create(
            email='testuser@email.com'
        )
        existing_subscribers = NewsletterSubscription.objects.filter(
            id=subscriber.id)
        self.assertEqual(len(existing_subscribers), 1)
        response = self.client.post(
            '/contact/newsletter_unsubscribe/',
            {'email': 'testuser@email.com'})
        existing_subscribers = NewsletterSubscription.objects.filter(
            id=subscriber.id)
        self.assertEqual(len(existing_subscribers), 0)

    def test_newsletter_unsubscribe_post_not_subscribed(self):
        """
        Tests the unsubscribe page and ensures that existing_subscribers
        length is = 1 if a user tries to unsubscribe without previously
        subscribing
        """
        subscriber = NewsletterSubscription.objects.create(
            email='testuser@email.com'
        )
        response = self.client.post(
            '/contact/newsletter_unsubscribe/',
            {'email': 'testuser2@email.com'}
        )
        existing_subscribers = NewsletterSubscription.objects.filter(
            id=subscriber.id)
        self.assertEqual(len(existing_subscribers), 1)

    def test_newsletter_unsubscribe_post_error(self):
        """
        Tests the unsubscribe form when the form is not valid
        """
        subscriber = NewsletterSubscription.objects.create(
            email='testuser@email.com'
        )
        response = self.client.post(
            '/contact/newsletter_unsubscribe/',
            {'email': ''}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Failed to unsubscribe. Please ensure the email you've entered is \
                    valid")
