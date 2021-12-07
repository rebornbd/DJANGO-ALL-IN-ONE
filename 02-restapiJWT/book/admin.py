from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'writer']
    list_display = ('title', 'writer', 'created', 'updated')
    list_filter = ['created', 'writer']
    search_fields = ['title', 'writer']

admin.site.register(Book, BookAdmin)
