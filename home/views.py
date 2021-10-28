from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from contact.models import Contact


def index(request):
    """
    A view to return the index page
    """
    # Returns the 8 latest blogs
    blogs = Blog.objects.order_by('-date')[:8]

    context = {
        'blogs': blogs,
    }
    return render(request, 'home/index.html', context)


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
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    return render(request, 'home/product-management.html')


@login_required
def contact_management(request):
    """
    A view to return all messages submitted from users
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'home/contact_management.html', context)


@login_required
def contact_detail(request, contact_id):
    """A view to display the contact message"""
    contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact': contact,
    }

    return render(request, 'home/contact_detail.html', context)


@login_required
def delete_contact(request, contact_id):
    """Delete an existing contact message"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, f'Contact message {contact.subject} deleted!')
    return redirect(reverse('contact_management'))
