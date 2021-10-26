from django.shortcuts import render
from .forms import NewsletterForm
from .models import NewsletterSubscription


def newsletter_register(request):

    print('hello world')
    
