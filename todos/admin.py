from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from todos.models import Todo


@register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
