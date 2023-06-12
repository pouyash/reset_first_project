from django.urls import path

from apis import views

urlpatterns = [
    path('books/', views.BookListApiView.as_view(), name='book_list_api'),


    path('todos/', views.TodoListApiView.as_view(), name='todo_api_list_view'),
    path('todos/<int:pk>', views.TodoDetailView.as_view(), name='todo_api_detail_view'),
]
