from django import forms
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        master_category = MasterCategory.objects.all()
        product_category = ProductCategory.objects.all()
        product_sub_category = ProductSubCategory.objects.all()

        master_category_friendly_names = [(mc.id, mc.get_master_friendly_name()) for mc in master_category]
        product_category_friendly_names = [(pc.id, pc.get_product_friendly_name()) for pc in product_category]
        product_sub_category_friendly_names = [(sc.id, sc.get_product_sub_friendly_name()) for sc in product_sub_category]

        self.fields['master_category'].choices = master_category_friendly_names
        self.fields['product_category'].choices = product_category_friendly_names
        self.fields['product_sub_category'].choices = product_sub_category_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-style-input'
