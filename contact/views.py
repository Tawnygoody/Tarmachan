from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import NewsletterForm
from .models import NewsletterSubscription


def newsletter_register(request):
    """
    A view to get the email address from the NewsletterForm.
    Checks whether the user has already subscribed, and
    redirects them to the page they were on if they have. 
    If not a confirm message and email is issued to the 
    user.
    """

    url = request.META.get('HTTP_REFERER')
    newsletter_form = NewsletterForm(request.POST)
    if newsletter_form.is_valid():
        if NewsletterSubscription.objects.filter(email=request.POST.get("email")).exists():
            messages.info(
                request,
                "This email address is already subscribed to the Tarmachan \
                    newsletter.")
            return HttpResponseRedirect(url)
        else:
            newsletter_form.save()
            messages.success(
                request,
                "You are now subscribed to the Tarmachan newsletter."
            )
            return HttpResponseRedirect(url)
    else:
        messages.error(
            request,
            "Failed to subscribe. Please ensure the email you've entered is \
                valid"
        )
        return HttpResponseRedirect(url)



    
