from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BookList(models.Model):
    book_name = models.CharField(max_length=100)
    img_path = models.ImageField(null=True)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    level = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class BookDetail(models.Model):
    BookList = models.ForeignKey(BookList, on_delete=models.CASCADE)
    content = models.TextField()
    page = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class QuizList(models.Model):
    BookList = models.ForeignKey(BookList, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class WordList(models.Model):
    QuizList = models.ForeignKey(QuizList, on_delete=models.CASCADE)
    word_name = models.CharField(max_length=30)
    img_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Users(AbstractUser):
    User_id = models.CharField(max_length=50)
    