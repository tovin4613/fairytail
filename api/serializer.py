from rest_framework import serializers
from product.models import BookList

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookList    
        fields = ['id', 'book_name', 'author', 'genre', 'level', 'created_at']