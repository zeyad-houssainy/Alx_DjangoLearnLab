﻿# Retrieve Operation

Command:
```python
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
#Expected Output:
#('1984', 'George Orwell', 1949)
