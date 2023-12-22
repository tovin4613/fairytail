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
    
class Post(models.Model):       #<-추가
    User_id = models.CharField(max_length=20)      #<-추가
    title = models.CharField(max_length=50)     #<-추가
    content = models.CharField(max_length=500)       #<-추가
    created_at = models.DateTimeField(auto_now_add=True)        #<-추가

    def __str__(self):      #<-추가
        return self.name        #<-추가

class comment(models.Model):
    Post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    User_id = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
class Media(models.Model):
    Post = models.ForeignKey(Post, related_name='Media', on_delete=models.CASCADE)
    media_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
class BookDetail(models.Model):
    BookList = models.ForeignKey(BookList, related_name='BookDetail', on_delete=models.CASCADE)
    content = models.TextField()
    page = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class QuizList(models.Model):
    BookList = models.ForeignKey(BookList, related_name='QuizList', on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class WordList(models.Model):
    QuizList = models.OneToOneField(QuizList, related_name='WordList', on_delete=models.CASCADE)
    word_name = models.CharField(max_length=30)
    img_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Users(AbstractUser):
    User_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class UserAudioList(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    QuizList = models.OneToOneField(QuizList, related_name='UserAudioList', on_delete=models.CASCADE)
    audio_path = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class AiAudioList(models.Model):
    QuizList = models.OneToOneField(QuizList, related_name='AiAudioList', on_delete=models.CASCADE)
    audio_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)