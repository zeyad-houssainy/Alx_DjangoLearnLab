from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian


class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        # Create authors
        author1, created = Author.objects.get_or_create(name="J.K. Rowling")
        author2, created = Author.objects.get_or_create(name="George Orwell")
        author3, created = Author.objects.get_or_create(name="Jane Austen")

        # Create books
        book1, created = Book.objects.get_or_create(
            title="Harry Potter and the Sorcerer's Stone",
            author=author1
        )
        book2, created = Book.objects.get_or_create(
            title="1984",
            author=author2
        )
        book3, created = Book.objects.get_or_create(
            title="Pride and Prejudice",
            author=author3
        )

        # Create libraries
        library1, created = Library.objects.get_or_create(name="Central Library")
        library2, created = Library.objects.get_or_create(name="University Library")

        # Add books to libraries
        library1.books.add(book1, book2)
        library2.books.add(book2, book3)

        # Create librarians
        librarian1, created = Librarian.objects.get_or_create(
            name="Alice Johnson",
            library=library1
        )
        librarian2, created = Librarian.objects.get_or_create(
            name="Bob Smith",
            library=library2
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write(f'Authors: {Author.objects.count()}')
        self.stdout.write(f'Books: {Book.objects.count()}')
        self.stdout.write(f'Libraries: {Library.objects.count()}')
        self.stdout.write(f'Librarians: {Librarian.objects.count()}')
