from .models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def query_books_by_author(author_name):
    """Query all books by a specific author"""
    
    try:
        # Get author first, then filter books
        books = Book.objects.filter(author__name=author_name)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")
        return Book.objects.none()

# Query 2: List all books in a library
def query_books_in_library(library_name):
    """List all books in a library"""
    
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"Books in {library.name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return Book.objects.none()


# Query 3: Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        
        print(f"Librarian for {library.name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'")
        return None


# Direct query examples:
# 
# 1. Query all books by a specific author:
# author_name = "Author Name"
# author = Author.objects.get(name=author_name)
# books = Book.objects.filter(author=author)
#
# 2. List all books in a library:
# library_name = "Library Name"
# library = Library.objects.get(name=library_name)
# books = library.books.all()
#
# 3. Retrieve the librarian for a library:
# library_name = "Library Name"
# library = Library.objects.get(name=library_name)
# librarian = Librarian.objects.get(library=library)
