from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.contrib import messages
from django.db.models import Q
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory
)
# Create your views here.


def all_products(request):
    """
    A view to return all products, including sorting
    and search queries
    """

    products = Product.objects.all()
    query = None
    master_category = None
    product_category = None
    product_sub_category = None

    if request.GET:
        if 'master_category' in request.GET:
            master_category = request.GET['master_category'].split(',')
            products = products.filter(
                master_category__name__in=master_category)
            master_category = MasterCategory.objects.filter(
                name__in=master_category
            )

        if 'product_category' in request.GET:
            product_category = request.GET['product_category'].split(',')
            products = products.filter(
                product_category__name__in=product_category)
            product_category = ProductCategory.objects.filter(
                name__in=product_category
            )

        if 'product_sub_category' in request.GET:
            product_sub_category = request.GET['product_sub_category'].split(',')
            products = products.filter(
                product_sub_category__name__in=product_sub_category)
            product_sub_category = ProductSubCategory.objects.filter(
                name__in=product_sub_category
            )

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description1__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_master_category': master_category,
        'current_product_category': product_category,
        'current_product_sub_category': product_sub_category,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to return individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
