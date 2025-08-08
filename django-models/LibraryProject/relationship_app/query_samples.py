# Query all books by a specific author.
from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (by name):
def get_books_by_author(author_name):
	return Book.objects.filter(author__name=author_name)

# 2. List all books in a library (by library name):
def get_books_in_library(library_name):
	try:
		library = Library.objects.get(name=library_name)
		return library.books.all()
	except Library.DoesNotExist:
		return []

# 3. Retrieve the librarian for a library (by library name):
def get_librarian_for_library(library_name):
	try:
		library = Library.objects.get(name=library_name)
		return Librarian.objects.get(library=library)
	except (Library.DoesNotExist, Librarian.DoesNotExist):
		return None
