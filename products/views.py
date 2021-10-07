from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory, Clearance
)
from .forms import ProductForm
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
    clearance = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

        if 'clearance' in request.GET:
            clearance = request.GET['clearance'].split(',')
            products = products.filter(
                clearance__name__in=clearance)
            clearance = Clearance.objects.filter(
                name__in=clearance
            )

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description1__icontains=query)
            products = products.filter(queries)\

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_master_category': master_category,
        'current_product_category': product_category,
        'current_product_sub_category': product_sub_category,
        'current_clearance': clearance,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to return individual product details
    """

    product = get_object_or_404(Product, pk=product_id)
    savings = None
    percentage_savings = None

    if product.clearance:
        if product.clearance_price:
            savings = product.price - product.clearance_price
            percentage_savings_dec = ((product.price - product.clearance_price)/product.price) * 100
            percentage_savings = round(percentage_savings_dec, 0)

    context = {
        'product': product,
        'savings': savings,
        'percentage_savings': percentage_savings
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only the team at Tarmachan can access this.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only the team at Tarmachan can access this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only the team at Tarmachan can access this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
