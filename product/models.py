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
    User_id = models.CharField()      #<-추가
    title = models.CharField()     #<-추가
    content = models.CharField()       #<-추가
    created_at = models.DateTimeField(auto_now_add=True)        #<-추가

    def __str__(self):      #<-추가
        return self.name        #<-추가

class comment(models.Model):
    Post_id = models.IntegerField()
    User_id = models.CharField()
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    
class Media(models.Model):
    Post_id = models.IntegerField()
    media_path = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
