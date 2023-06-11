from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from book.models import Book


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'author', 'isbn',)
