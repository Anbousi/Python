from django.shortcuts import redirect, render
from books_authors_app.models import *

# Create your views here.
def main(request):
    context = {
        'Books' : Book.objects.all()
    }
    return render(request, 'Add_Book.html', context)

def add_book(request):
    add_book1(request.POST['book'] , request.POST['description'])
    return redirect('/')

def book_show(request , id):
    the_book = Book.objects.get(id=id)
    book = {
        'this_book': the_book,
        'authers': the_book.author.all(),
        'Authors' : Author.objects.all()
    }
    return render(request, 'book_show.html' , book)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'Add_Author.html' , context)

def add_author(request):
    add_authors1(request.POST['first_name'] , request.POST['last_name']  , request.POST['notes'])
    return redirect('/authors')

def authors_show(request , id):
    auth = Author.objects.get(id=id)
    request.session['id'] = id
    author = {
        'this_author': auth,
        'books': auth.books.all(),
        'Books' : Book.objects.all()
    }
    return render(request, 'author_show.html' , author)

def select_book(request):
    my_author = Author.objects.get(id = request.session['id'])
    Boook = request.POST['select_book1']
    create_book(my_author,Boook)
    return redirect('/authors')

def select_author(request):
    my_book = Book.objects.get(id = request.session['id'])
    return redirect('/')


