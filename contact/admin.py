from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterAdmin(admin.ModelAdmin):
    model = NewsletterSubscription
    list_display = (
        "email",
    )


admin.site.register(NewsletterSubscription, NewsletterAdmin)


