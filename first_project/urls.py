from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('apis/', include('apis.urls')),
    path('todos/', include('todos.urls')),
]
