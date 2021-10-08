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
        placeholders = {
            "title": "Title",
            "subheading1": "Paragraph 1 Subheading",
            "para1": "Paragraph 1",
            "subheading2": "Paragraph 2 Subheading",
            "para2": "Paragraph 2",
            "subheading3": "Paragraph 3 Subheading",
            "para3": "Paragraph 3",
            "subheading4": "Paragraph 4 Subheading",
            "para4": "Paragraph 4",
            "subheading5": "Paragraph 5 Subheading",
            "para5": "Paragraph 5",
            "subheading6": "Paragraph 6 Subheading",
            "para6": "Paragraph 6",
            "subheading7": "Paragraph 7 Subheading",
            "para7": "Paragraph 7",
            "subheading8": "Paragraph 8 Subheading",
            "para8": "Paragraph 8",
            "subheading9": "Paragraph 9 Subheading",
            "para9": "Paragraph 9",
            "image_caption1": "Caption for Main Image",
            "image_caption2": "Caption for Parallax Image",
            "image_caption3": "Caption for Content Image",
            "author": "Author",
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-style-input'
