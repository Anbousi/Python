from django.shortcuts import redirect, render
from django.contrib import messages
from . import models


def home(request):
    print("I am at the start of homr")
    if 'name' in request.session: #if user already logged in before
        print("**************************")
        this_user = models.get_user(request.session['email'])
        print(this_user[0].email)

        context = {
            'all_books': models.get_all_books(),
            'this_user': models.get_this_user(request.session['email'])
        }
        return render(request , 'home.html' , context)
    return redirect('/')
    
def log_reg(request):

    if 'name' in request.session: #if user already logged in before
        return redirect('/books')

    return render(request,'login.html')

def check(request):
    if request.method == 'POST':
        in_data = request.POST
        if in_data['log_reg'] == 'registration':
            errors = models.create_user(in_data)
            if len(errors)>0:
                for key,value in errors.items():
                    messages.error(request,value)
                return redirect('/')
            if 'login' not in request.session: #if user already logged in before
                request.session['name'] = request.POST['f_name']
                request.session['email'] = request.POST['email']
                request.session['user'] = models.get_this_user(request.POST['email']).id
            
            return redirect('/books')
        elif in_data['log_reg'] == 'login':
            if request.method == 'POST':
                print("33333333333333333333333333333333")
                errors = models.login_user(request.POST)
                if len(errors)>0:
                    for key,value in errors.items():
                        messages.error(request,value)
                    return redirect('/')
                print("4444444444444444444444444444")
                user = models.get_user(request.POST['email'])
                if 'login' not in request.session: #if user already logged in before
                    request.session['name'] = user[0].first_name
                    request.session['email'] = user[0].email
                    request.session['user'] = user[0].id
                    print(request.session['name'])
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    uploaded_by = request.session['user']
    new_book = models.add_book(title , desc , uploaded_by)
    return redirect('/books/')

def add_favourite(request, book_id):
    models.add_favourite(request.session['user'] , book_id)
    return redirect('/books/')

def view_book(request , book_id):
    
    context = {
        'this_book': models.get_book(book_id),
        'this_user': models.get_user(request.session['email'])
    }
    return render(request, 'book.html' , context)

def update(request,book_id):
    desc = request.POST['desc']
    models.update(book_id , desc)
    return redirect(f'/books/{book_id}')

def delete(request , book_id):
    models.delete(book_id)
    return redirect('/books/')

def unfollow(request, book_id):
    user_id = request.session['user']
    models.unfollow(user_id , book_id)
    return redirect(f'/books/{book_id}')

