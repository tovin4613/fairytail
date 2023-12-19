from django.db import models

# Create your models here.
class BookList(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    level = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):       #<-추가
    User_id = models.CharField(max_length=100)      #<-추가
    title = models.CharField(max_length=20)     #<-추가
    content = models.CharField(max_length=20)       #<-추가
    created_at = models.DateTimeField(auto_now_add=True)        #<-추가

    def __str__(self):      #<-추가
        return self.name        #<-추가