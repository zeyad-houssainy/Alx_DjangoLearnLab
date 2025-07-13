from django.db import models

class Book(models.Model):
    # CharField with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    # CharField with a maximum length of 100 characters.
    author = models.CharField(max_length=100)
    # IntegerField
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
