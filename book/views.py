from django.shortcuts import render
from django.views.generic import ListView

from book.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/books.html'
    context_object_name = 'books'