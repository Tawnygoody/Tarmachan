from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
]
