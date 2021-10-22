from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path(
        'product_management/', views.product_management,
        name='product_management'
    ),
]
