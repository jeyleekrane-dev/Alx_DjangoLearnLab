from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    pass


# Register the Book model with the custom admin class.
admin.site.register(Book, BookAdmin)


# Register your models here.
admin.site.register(Book)
