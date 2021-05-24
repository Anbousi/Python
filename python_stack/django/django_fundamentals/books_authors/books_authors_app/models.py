from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes= models.TextField()
    books = models.ManyToManyField(Book, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def add_book1(title , desc):
    Book.objects.create(title = title , description = desc)

def add_authors1(f_name, l_name , notes):
    Author.objects.create(first_name = f_name , last_name = l_name , notes= notes)

def create_book(my_author,Boook):
    added_book = Book.objects.get(id = Boook)
    my_author.books.add(added_book)

