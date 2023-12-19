from django.db import models

# Create your models here.
class BookList(models.Model):
    book_name = models.CharField(max_length=100)
    img = models.ImageField(null=True)
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