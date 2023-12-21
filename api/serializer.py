from rest_framework import serializers
from product.models import *

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['id', 'BookList_id', 'content', 'page', 'created_at']

class WordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordList
        fields = ['id', 'QuizList_id', 'word_name', 'img_path', 'created_at']

class AiAudioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiAudioList
        fields = ['id', 'QuizList_id', 'audio_path', 'created_at']

class QuizListSerializer(serializers.ModelSerializer):
    WordList = WordListSerializer(many=False, read_only=True)
    AiAudioList = AiAudioListSerializer(many=False, read_only=True)

    class Meta:
        model = QuizList
        fields = ['id', 'BookList_id', 'category', 'question', 'answer', 'created_at', 'WordList', 'AiAudioList']

class BookSerializer(serializers.ModelSerializer):
    BookDetail = BookDetailSerializer(many=True, read_only=True)
    QuizList = QuizListSerializer(many=True, read_only=True)
    
    class Meta:
        model = BookList
        fields = ['id', 'book_name', 'img_path', 'author', 'genre', 'level', 'created_at', 'BookDetail', 'QuizList']