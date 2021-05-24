from django.contrib import admin
from .models import Directory


class DirectoryAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'book',
        'author',
        'genre',
        'text',
        'created_date',
        'published_date'
    ]


admin.site.register(Directory, DirectoryAdmin)
