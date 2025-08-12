from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.

# lists all books stored in the database.


def list_books(request):
    """View that lists all books using HTML template"""
    # Use select_related to optimize database queries by fetching author data in one query
    books = Book.objects.all()
    context = {'books': books}
    # Updated template path to be consistent with directory structure
    return render(request, 'relationship_app/list_books.html', context)


# displays details for a specific library, listing all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    # Updated template path to be consistent with list_books view
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



