from django.shortcuts import render
from rest_framework import viewsets
from product.models import BookList
from .serializer import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer