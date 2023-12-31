from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author