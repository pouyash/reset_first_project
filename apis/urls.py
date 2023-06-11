from django.urls import path

from apis import views

urlpatterns = [
    path('books/', views.BookListApiView.as_view(), name='book_list_api'),
]
