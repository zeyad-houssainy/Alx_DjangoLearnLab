from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian


class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        # Create authors
        author1, created = Author.objects.get_or_create(name="J.K. Rowling")
        author2, created = Author.objects.get_or_create(name="George Orwell")
        author3, created = Author.objects.get_or_create(name="Jane Austen")

        # Create books with publication years
        book1, created = Book.objects.get_or_create(
            title="Harry Potter and the Sorcerer's Stone",
            author=author1,
            defaults={'publication_year': 1997}
        )
        book2, created = Book.objects.get_or_create(
            title="1984",
            author=author2,
            defaults={'publication_year': 1949}
        )
        book3, created = Book.objects.get_or_create(
            title="Pride and Prejudice",
            author=author3,
            defaults={'publication_year': 1813}
        )
        
        # Create additional books for more comprehensive testing
        book4, created = Book.objects.get_or_create(
            title="Animal Farm",
            author=author2,
            defaults={'publication_year': 1945}
        )
        book5, created = Book.objects.get_or_create(
            title="Harry Potter and the Chamber of Secrets",
            author=author1,
            defaults={'publication_year': 1998}
        )
        book6, created = Book.objects.get_or_create(
            title="Emma",
            author=author3,
            defaults={'publication_year': 1815}
        )

        # Create libraries with more books
        library1, created = Library.objects.get_or_create(name="Central Library")
        library2, created = Library.objects.get_or_create(name="University Library")
        library3, created = Library.objects.get_or_create(name="Community Library")

        # Add books to libraries for comprehensive testing
        library1.books.add(book1, book2, book4)  # Central Library: Harry Potter 1, 1984, Animal Farm
        library2.books.add(book2, book3, book5)  # University Library: 1984, Pride and Prejudice, Harry Potter 2
        library3.books.add(book3, book6)         # Community Library: Pride and Prejudice, Emma

        # Create librarians for each library
        librarian1, created = Librarian.objects.get_or_create(
            name="Alice Johnson",
            library=library1
        )
        librarian2, created = Librarian.objects.get_or_create(
            name="Bob Smith",
            library=library2
        )
        librarian3, created = Librarian.objects.get_or_create(
            name="Carol Davis",
            library=library3
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully created comprehensive mock library data!')
        )
        self.stdout.write(f'Authors: {Author.objects.count()}')
        self.stdout.write(f'Books: {Book.objects.count()}')
        self.stdout.write(f'Libraries: {Library.objects.count()}')
        self.stdout.write(f'Librarians: {Librarian.objects.count()}')
        
        # Display some sample data for verification
        self.stdout.write('\n' + self.style.SUCCESS('Sample Libraries and their books:'))
        for library in Library.objects.all():
            self.stdout.write(f'\n{library.name}:')
            for book in library.books.all():
                self.stdout.write(f'  - {book.title} by {book.author.name} ({book.publication_year})')
        self.stdout.write(f'Libraries: {Library.objects.count()}')
        self.stdout.write(f'Librarians: {Librarian.objects.count()}')
