from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for the admin interface
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')
