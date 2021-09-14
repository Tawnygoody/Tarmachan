from django.contrib import admin
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'master_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class MasterCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(MasterCategory, MasterCategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
