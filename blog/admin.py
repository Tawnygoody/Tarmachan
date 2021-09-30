from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'para1',
        'para2',
        'para3',
        'author',
        'date',
    )


admin.site.register(Blog, BlogAdmin)
