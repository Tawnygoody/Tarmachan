from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<blog_id>', views.blog_detail, name='blog_detail'),
]
