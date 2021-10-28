from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path(
        'product_management/', views.product_management,
        name='product_management'
    ),
    path(
        'contact_management/', views.contact_management,
        name='contact_management'
    ),
    path(
        '<int:contact_id>/', views.contact_detail,
        name='contact_detail'
    ),
    path(
        'delete_contact/<int:contact_id>', views.delete_contact,
        name='delete_contact'
    )
]
