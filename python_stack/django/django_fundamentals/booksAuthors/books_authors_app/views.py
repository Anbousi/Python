from django.shortcuts import redirect, render 
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_book_template(request):
    context = {
        "all_books": all_books()
    }
    return render(request,'add_book.html' , context)

def add_author_template(request):
    context = {
        "all_authors": all_authors()
    }
    return render(request,'add_author.html' , context)

def create_book(request):
    if request.method == "POST":
        add_book(request.POST)
    return redirect('/')

def create_author(request):
    if request.method == "POST":
        add_author(request.POST)
    return redirect('/author')


def view_book(request , id):
    this_book = get_book(id)
    context = {
        "book": this_book,
        "book_authors": book_authors(id),
        "all_authors": all_authors()
    }
    return render(request ,'view_book.html' , context)

def view_author(request , id):
    this_author = get_author(id)
    context = {
        "author": this_author,
        "author_books": author_books(id),
        "all_books": all_books()
    }
    return render(request ,'view_author.html' , context)

def add_author_to_book(request,id):
    # print('0000'*30)
    # print(id)
    if request.method == "POST":
        # print(request.POST['author_id'])
        add_author_book(id, request.POST['author_id'])
    return redirect (f'/books/{id}')

def add_book_to_author(request,id):
    if request.method == "POST":
        add_book_author(id, request.POST['book_id'])
    return redirect (f'/authors/{id}')
