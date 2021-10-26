from django.contrib import admin
from .models import NewsletterSubscription, Contact


class NewsletterAdmin(admin.ModelAdmin):
    model = NewsletterSubscription
    list_display = (
        'email',
    )


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'subject', 'email', 'name',
    )


admin.site.register(NewsletterSubscription, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
