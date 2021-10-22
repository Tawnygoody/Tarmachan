from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from .models import (
    Product, MasterCategory, ProductCategory, ProductSubCategory, Clearance,
    Comment
)
from .forms import ProductForm, CommentForm


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
            # If the search field was left blank
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

    # Gets the product from the database
    product = get_object_or_404(Product, pk=product_id)
    # Gets the comments attached to the product from the database
    comments = Comment.objects.filter(product_id=product_id)
    # Check to see if there are any comments and updates
    # the product rating based on the average rating
    if comments:
        ratings = comments.count()
        rating_avg = comments.aggregate(Avg('rating'))
        rating = round(rating_avg.get('rating__avg'), 2)
        product.rating = rating
        product.save()
    # if there are no ratings sets product rating to 0
    else:
        ratings = 0
        rating = 0

    savings = None
    percentage_savings = None

    # Checks to see if the product is in clearance and
    # calculates the savings price and percentage
    if product.clearance:
        if product.clearance_price:
            savings = product.price - product.clearance_price
            percentage_savings_dec = (
                (product.price - product.clearance_price)/product.price
            ) * 100
            percentage_savings = round(percentage_savings_dec, 0)

    context = {
        'product': product,
        'savings': savings,
        'percentage_savings': percentage_savings,
        'comments': comments,
        'ratings': ratings,
        'rating': rating
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the site """
    # User check as only superusers can add products
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_comment(request, product_id):
    """Add a comment"""

    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        # creates a relation with Comment model
        data = Comment()
        # gets the form input data
        data.subject = form['subject'].value()
        data.comment = form['comment'].value()
        data.rating = form['rating'].value()
        data.product_id = product_id
        current_user = request.user
        data.user_id = current_user.id
        # saves the comment
        data.save()
        messages.success(request, 'Successfully added comment!')
        return HttpResponseRedirect(url)
    else:
        form = CommentForm()

    return HttpResponseRedirect(url)


@login_required
def delete_comment(request, comment_id):
    """ Delete an exisiting Comment """

    comment = get_object_or_404(Comment, pk=comment_id)
    product = get_object_or_404(Product, pk=comment.product_id)
    url = request.META.get('HTTP_REFERER')

    # only the user who left the comment or superuser can delete comments
    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
        reviews = Comment.objects.filter(product=product)
        # Updates the product rating when a comment is deleted
        if reviews:
            rating_avg = reviews.aggregate(Avg("rating"))
            rating = round(rating_avg.get('rating__avg'), 2)
            product.rating = rating
        # else sets the product rating to 0
        else:
            product.rating = 0

        product.save()

        messages.success(
            request,
            f'Review {comment.subject} has been deleted!'
        )
        return HttpResponseRedirect(url)
    else:
        messages.error(
            request,
            "Only the team at Tarmachan and the reviewer can access this."
        )
        return HttpResponseRedirect(url)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product """

    # User check as only superusers can add products
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
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

    # User check as only superusers can add products
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
