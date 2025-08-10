from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Author, Library, Librarian

# Create your views here.

# lists all books stored in the database.
def List_books(request):
    """View that lists all books using HTML template"""
    books = Book.objects.select_related('author').all()
    print(f"DEBUG: Found {books.count()} books")  # Debug info
    for book in books:
        print(f"DEBUG: Book: {book.title} by {book.author.name}")
    
    context = {
        'books': books
    }
    return render(request, 'list_books.html', context)


# displays details for a specific library, listing all books available in that library.
class Library_books(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['books'] = library.books.all()  # Get all books in this library
        return context
