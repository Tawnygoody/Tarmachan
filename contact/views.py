from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import NewsletterForm, ContactForm, NewsletterUnsubscribeForm
from .models import NewsletterSubscription


def contact(request):
    """
    A view to display the contact us page and contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            name = request.POST.get('name')
            form.save()
            messages.success(
                request,
                f'Thanks {name}! {subject} has been sent to the \
                    Tarmachan team.'
            )
        else:
            messages.error(
                request,
                "Failed to send message, please ensure all fields are correct"
            )

    form = ContactForm()

    context = {
        "form": form
    }
    return render(request, 'contact/contact.html', context)


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
                "You are now subscribed to the Tarmachan newsletter. \
                    We have sent an email confirmation to you."
            )
            # Sending email confirmation of subscription
            data = newsletter_form.save()
            subscriber_email = data.email
            subject = render_to_string(
                'contact/confirmation_emails/newsletter_subscription_subject.txt',
            )
            body = render_to_string(
                'contact/confirmation_emails/newsletter_subscription_body.txt',
                {'data': data,
                 'tarmachan_email': settings.DEFAULT_FROM_EMAIL}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [subscriber_email],
            )
            return HttpResponseRedirect(url)
    else:
        messages.error(
            request,
            "Failed to subscribe. Please ensure the email you've entered is \
                valid"
        )
        return HttpResponseRedirect(url)


def newsletter_unsubscribe(request):
    template = 'contact/newsletter_unsubscribe.html'
    if request.method == "POST":
        unsubscribe_form = NewsletterUnsubscribeForm(request.POST)
        if unsubscribe_form.is_valid():
            if NewsletterSubscription.objects.filter(email=request.POST.get("email")).exists():
                email = request.POST.get('email')
                NewsletterSubscription.objects.filter(email=request.POST.get("email")).delete()
                messages.success(
                    request,
                    f'{email} has been removed from our mailing list'
                )
                subject = render_to_string(
                    'contact/confirmation_emails/newsletter_unsubscribe_subject.txt'
                )
                body = render_to_string(
                    'contact/confirmation_emails/newsletter_unsubscribe_body.txt',
                    {'email': email,
                     'tarmachan_email': settings.DEFAULT_FROM_EMAIL}
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    email,
                )
                return redirect(reverse('home'))
            else:
                messages.error(
                    request,
                    'Sorry! This email is not in our mailing list.'
                )
        else:
            messages.error(
                    request,
                    "Failed to unsubscribe. Please ensure the email you've entered is \
                    valid"
                )

    unsubscribe_form = NewsletterUnsubscribeForm()

    context = {
        "unsubscribe_form": unsubscribe_form
    }

    return render(request, template, context)
