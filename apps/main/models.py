# apps/main/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30, 
                            verbose_name='Автор')
    birthdate = models.DateField(auto_now_add=True, 
                            verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50,
                                verbose_name='Название книги')
    publication_year = models.DateField(auto_now_add=True,
                                verbose_name='Год публикации')
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                                verbose_name='Автор')
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                            verbose_name='Книга')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, 
                            verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанры книг'

class Genre(models.Model):
    name = models.CharField(max_length=30, 
                            verbose_name='Жанр')
    books = models.ManyToManyField(Book, through='BookGenre',
                            verbose_name='Книги')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
