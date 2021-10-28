from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


def blog(request):
    """ A view to display all blogs """
    # Get all the blog posts in the database and order
    # so latest blogs appear first
    blogs = Blog.objects.all().order_by('-date')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to display individual blogs """
    # Get a specified blog from the database
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """ A view to add a blog to the site"""
    # Only superuser's can access this view
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added Blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(
                request,
                'Failed to add blog. Please ensure the form is valid.'
            )
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ A view to edit a Blog """
    # Only superuser's can access this view
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    # Get the blog post using the given Id
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(
                request,
                'Failed to update blog. Please ensure the form is valid.'
            )
    else:
        # If the request is a get request:
        # Populate the blog form with the existing data in the database
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete an exisiting Blog """
    # Only superuser's can access this view
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry! Only the team at Tarmachan can access this.'
        )
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))
