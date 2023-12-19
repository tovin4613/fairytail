from rest_framework import serializers
from product.models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookList    
        fields = ['id', 'book_name', 'img', 'author', 'genre', 'level', 'created_at']

class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookDetail    
        fields = ['id', 'BookList_id', 'content', 'page', 'created_at']