from django import forms
from .models import NewsletterSubscription



class NewsletterForm(forms.ModelForm):
    """
    Create a form for superusers to add a blog
    """

    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["placeholder"] = "Email *"
        self.fields["email"].widget.attrs['class'] = "subscribe-input"
        self.fields["email"].label = False
