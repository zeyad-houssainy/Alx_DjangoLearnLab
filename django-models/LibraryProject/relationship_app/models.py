from django.db import models

# Create your models here.


# class Book(models.Model):
#     # CharField with a maximum length of 200 characters.
#     title = models.CharField(max_length=200)
#     # CharField with a maximum length of 100 characters.
#     author = models.CharField(max_length=100)
#     # IntegerField
#     publication_year = models.IntegerField()

#     def __str__(self):
#         return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
