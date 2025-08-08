<!-- Selecting all  -->
Book.objects.all()
<!-- selecting specific  -->
Book.objects.filter(title="1984", author="George Orwell", publication_year=1949)
<!-- selecting specific  -->
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year