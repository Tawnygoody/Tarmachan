from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    A view to return the products in the bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping
    bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the bag from the session if it exists
    # or initialize it to an empty dict if not
    bag = request.session.get('bag', {})

    # Check to see if product has sizes
    if size:
        # Check to see if product is already in bag
        if item_id in list(bag.keys()):
            # Check to see if product with specified size is already in bag
            # and updates the quantity if it is
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to \
                    {bag[item_id]["items_by_size"][size]}'
                )
            # If not adds product to bag
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag'
                )
        # If not adds product to bag
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag'
            )
    # For products without sizes
    else:
        # Check to see if product already in bag
        if item_id in list(bag.keys()):
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        # Adds product to bag
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Put the bag variable in the session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the bag from the session if it exists
    # or initialize it to an empty dict if not
    bag = request.session.get('bag', {})

    # For products with sizes
    if size:
        # Check to see if quantity is greater than 0
        # if it is updates quantity to specified amount
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to \
                {bag[item_id]["items_by_size"][size]}'
            )
        # If quantity is 0 then removes the product from the bag
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
    # For products without sizes
    else:
        # Check to see if quantity is greater than 0
        # if it is updates quantity to specified amount
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        # If quantity is 0 then removes the product from the bag
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove an item from the shopping bag
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Get the bag from the session if it exists
        # or initialize it to an empty dict if not
        bag = request.session.get('bag', {})

        # Removes product for products with sizes
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request,
                    f'Removed size {size.upper()} {product.name} from your bag'
                )
        # Removes product for products without sizes
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
