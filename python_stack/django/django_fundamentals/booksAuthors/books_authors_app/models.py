from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    note = models.TextField()
    books = models.ManyToManyField(Books, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def all_books():
    all_books = Books.objects.all()
    return all_books

def all_authors():
    all_authors = Authers.objects.all()
    return all_authors

def add_book(data):
    Books.objects.create(title = data['title'] , desc = data['desc'])

def add_author(data):
    Authers.objects.create(first_name = data['f_name'] , last_name = data['l_name'] , note = data['note'])

def get_book(id):
    this_book = Books.objects.get(id = id)
    return this_book

def get_author(id):
    this_author = Authers.objects.get(id = id)
    return this_author

def book_authors(id):
    this_book =  get_book(id)
    authors = this_book.authers.all()
    return authors

def author_books(id):
    this_author =  get_author(id)
    books = this_author.books.all()
    return books

def add_author_book(book_id, author_id):
    this_book = get_book(book_id)
    this_author = get_author(author_id)
    this_book.authers.add(this_author)

def add_book_author(author_id, book_id):
    this_book = get_book(book_id)
    this_author = get_author(author_id)
    this_author.books.add(this_book)
