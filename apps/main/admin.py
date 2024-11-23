from django.contrib import admin
from .models import Book, Author, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
