from django.http import JsonResponse
from rest_framework import viewsets

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookListViewset(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
