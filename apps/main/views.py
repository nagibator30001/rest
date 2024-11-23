from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Book, Author, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer

class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreListApiView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreCreateApiView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
