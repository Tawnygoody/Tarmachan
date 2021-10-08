from django import forms
from .models import Blog
from .widgets import CustomClearableFileInput, CustomClearableFileInput2, CustomClearableFileInput3


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    image1 = forms.ImageField(label='Main Image', required=False, widget=CustomClearableFileInput)
    image2 = forms.ImageField(label='Parallax Image', required=False, widget=CustomClearableFileInput2)
    image3 = forms.ImageField(label='Content Image', required=False, widget=CustomClearableFileInput3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-style-input'
