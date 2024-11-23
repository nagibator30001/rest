from django.urls import path
from .views import BookListApiView, BookCreateApiView, AuthorListApiView, AuthorCreateApiView, GenreListApiView, GenreCreateApiView

urlpatterns = [
    path('api/books/', BookListApiView.as_view(), name='book-list'),
    path('api/books/create/', BookCreateApiView.as_view(), name='book-create'),
    path('api/authors/', AuthorListApiView.as_view(), name='author-list'),
    path('api/authors/create/', AuthorCreateApiView.as_view(), name='author-create'),
    path('api/genres/', GenreListApiView.as_view(), name='genre-list'),
    path('api/genres/create/', GenreCreateApiView.as_view(), name='genre-create'),
]
