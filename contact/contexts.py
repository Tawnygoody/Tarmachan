from .forms import NewsletterForm


def newsletter_subscription_form(request):
    newsletter_form = NewsletterForm()

    context = {
        'newsletter_form': newsletter_form,
    }

    return context
