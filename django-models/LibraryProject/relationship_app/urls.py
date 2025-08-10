from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = "Zeyad Admin Page"
admin.site.index_title = "Index_title"

urlpatterns = [
    # path("", views.index, name="index"),
    path("books/", views.List_books, name="List_books"),
    path("library_books/",
         views.Library_books.as_view(), name="library_books"),
]
