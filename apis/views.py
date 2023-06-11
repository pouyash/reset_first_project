from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from apis.serializers import BookSerializer
from book.models import Book


class BookListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
