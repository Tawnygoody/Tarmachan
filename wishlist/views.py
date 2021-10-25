from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product


@login_required
def wishlist(request):
    """
    A view to return products which have been added
    to the user's wishlist
    """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can access the wishlist'
        )
        return redirect(reverse('home'))

    products = Product.objects.filter(user_wishlist=request.user)
    context = {
        'products': products
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Allows registered users to add and remove products from their wishlist
    """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can add products to their wishlist'
        )
        return redirect(reverse('home'))

    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, pk=product_id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.success(request, f'{product.name} has been removed from your wishlist')
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, f'{product.name} has been added to your wishlist')
    return HttpResponseRedirect(url)
