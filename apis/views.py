from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from apis.serializers import BookSerializer
from book.models import Book
from todos.models import Todo
from todos.serializers import TodoSerializer


class BookListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




# Todo Apis *****************************************

class TodoListApiView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


