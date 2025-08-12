from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Author, Library, Librarian

# Create your views here.

# lists all books stored in the database.


def list_books(request):
    """View that lists all books using HTML template"""
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'list_books.html', context)


# displays details for a specific library, listing all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'



