from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User


class MasterCategory(models.Model):
    """
    This allows the grouping of products for men,
    women & equipment.
    """

    class Meta:
        verbose_name_plural = 'Master Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_master_friendly_name(self):
        return self.friendly_name


class ProductCategory(models.Model):
    """
    This allows the grouping of products for
    product categories
    """

    class Meta:
        verbose_name_plural = 'Product Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_product_friendly_name(self):
        return self.friendly_name


class ProductSubCategory(models.Model):
    """
    This allows the grouping of products for
    product sub categories
    """

    class Meta:
        verbose_name_plural = 'Product Sub Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_product_sub_friendly_name(self):
        return self.friendly_name


class Clearance(models.Model):
    """
    This allows the grouping of products that are in clearance
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_clearance_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Product Model contains the detailed product information
    with foreign keys to the category models
    """
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=254,
    )
    description1 = models.TextField(
        max_length=200,
    )
    description2 = models.TextField(
        null=True,
        blank=True
    )
    spec1 = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    spec2 = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    spec3 = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    spec4 = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    clearance = models.ForeignKey(
        'Clearance',
        null=True,
        blank=True,
        default=2,
        on_delete=models.SET_NULL,
    )
    clearance_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    master_category = models.ForeignKey(
        'MasterCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    product_category = models.ForeignKey(
        'ProductCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    product_sub_category = models.ForeignKey(
        'ProductSubCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    user_wishlist = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ This model contains product comment information"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(max_length=250, null=False, blank=False)
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
