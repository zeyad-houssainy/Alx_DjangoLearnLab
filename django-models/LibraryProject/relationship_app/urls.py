from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = "Zeyad Admin Page"
admin.site.index_title = "Index_title"

urlpatterns = [
    path("", views.index, name="index"),
]
