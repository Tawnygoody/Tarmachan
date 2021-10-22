from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Override the init methood of the form to allow customization
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Dictionary of placeholders to populate form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Cursor is automatically set to the Full Name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                # Adds a asterisk to fields that are required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Sets the placeholder to the values outlined in the
                # placeholders dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds a CSS class to style the inputs
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removes the labels
            self.fields[field].label = False
