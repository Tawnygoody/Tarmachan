from django.urls import path
from . import views

urlpatterns = [
    path('newsletter_register/', views.newsletter_register, name='newsletter_register'),
    path('newsletter_unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
]
