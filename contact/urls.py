from django.urls import path
from . import views

urlpatterns = [
    path('newsletter_register/', views.newsletter_register, name='newsletter_register')
]
