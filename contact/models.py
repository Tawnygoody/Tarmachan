from django.db import models


class NewsletterSubscription(models.Model):

    email = models.EmailField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.email
