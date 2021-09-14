from django.contrib import admin
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory
)

# Register your models here.
admin.site.register(Product)
admin.site.register(MasterCategory)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
