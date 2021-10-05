from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')


def about_us(request):
    """
    A view to return the about us page
    """
    return render(request, 'home/about-us.html')


@login_required
def product_management(request):
    """
    A view to return product Managment Page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only the team at Tarmachan can access this.')
        return redirect(reverse('home'))

    return render(request, 'home/product-management.html')
