from django import forms
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory,
    Clearance, Comment)
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """Form to add products"""

    class Meta:
        model = Product
        fields = (
            'sku', 'name', 'description1', 'description2',
            'spec1', 'spec2', 'spec3', 'spec4', 'price', 'clearance',
            'clearance_price', 'rating', 'sizes', 'master_category',
            'product_category', 'product_sub_category', 'image',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        master_category = MasterCategory.objects.all()
        product_category = ProductCategory.objects.all()
        product_sub_category = ProductSubCategory.objects.all()
        clearance = Clearance.objects.all()

        # Updates the categories to use friendly names
        master_category_friendly_names = [(
            mc.id, mc.get_master_friendly_name()) for mc in master_category]
        product_category_friendly_names = [(
            pc.id, pc.get_product_friendly_name()) for pc in product_category]
        product_sub_category_friendly_names = [(
            sc.id,
            sc.get_product_sub_friendly_name()) for sc in product_sub_category]
        clearance_friendly_names = [(
            cl.id, cl.get_clearance_name()) for cl in clearance]

        self.fields['master_category'].choices = master_category_friendly_names
        self.fields['product_category'].choices = (
            product_category_friendly_names)
        self.fields['product_sub_category'].choices = (
            product_sub_category_friendly_names)
        self.fields['clearance'].choices = clearance_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-style-input'


class CommentForm(forms.ModelForm):
    """Form for logged in users to leave a review"""

    class Meta:
        model = Comment
        fields = ('subject', 'comment', 'rating')
