from django import forms
from .models import NewsletterSubscription, Contact


class NewsletterForm(forms.ModelForm):
    """
    Create a form for any user to subscribe to the company
    newsletter
    """

    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email *"
        self.fields["email"].widget.attrs['class'] = "subscribe-input"
        # updates the input id to a unique id for the page
        self.fields["email"].widget.attrs['id'] = "newsletter-email"
        self.fields["email"].label = False


class NewsletterUnsubscribeForm(forms.ModelForm):
    """
    Create a form for any user to unsubscribe to the company
    newsletter
    """

    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["placeholder"] = "Email *"
        self.fields["email"].widget.attrs['class'] = "product-style-input"
        self.fields["email"].label = False


class ContactForm(forms.ModelForm):
    """
    Create a form for any user to contact the company
    """

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }

        for field in self.fields:
            # Adds a asterisk to fields that are required
            placeholder = f'{placeholders[field]} *'
            # Sets the placeholder to the values outlined in the
            # placeholders dictionary
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds a CSS class to style the inputs
            self.fields[field].widget.attrs['class'] = 'product-style-input'
            # Removes the labels
            self.fields[field].label = False
