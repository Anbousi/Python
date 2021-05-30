from django.contrib.messages.api import error
from django.contrib import messages
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
import re
from datetime import datetime
import bcrypt


# Create your models here.

class UsersManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        if len(post_data['f_name']) < 2:
            errors['f_name'] = "First name should be at least 2 Chars."

        if len(post_data['l_name']) < 2:
            errors['l_name'] = "Last name should be at least 2 Chars."
        
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 Chars."
        
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Confirm Password is not matching"
        
        return errors

    def book_validation(self,title,desc):
        errors={}
        if len(title) < 1:
            errors['title'] = "Title should not be empty."

        if len(desc) < 5:
            errors['desc'] = "Description should be at least 5 Chars."
        
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    liked_by = models.ManyToManyField(User,related_name='fav_books')
    uploaded_by = models.ForeignKey(User , related_name='uploaded_books' , on_delete=models.CASCADE)
    objects = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(data):
    errors = User.objects.basic_validator(data)
    db_email = User.objects.filter(email = data['email'])

    if db_email:
        errors['db_email'] = "This email is used."    
    
    if len(errors) == 0:
        #hash password before saving in database
        pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name = data['f_name'] , last_name = data['l_name'] , email = data['email'] , password = pw)    
    return errors

def get_user(user):
    this_user = User.objects.filter(email = user)
    return this_user

def get_this_user(email):
    this_user = User.objects.get(email = email)
    return this_user

def login_user(data):
    errors={}
    this_user = get_user(data['email'])
    if len(this_user)>0:
        pw = this_user[0].password
        in_pw =  bcrypt.checkpw(data["password"].encode(), pw.encode())
        if in_pw == True:
                return errors
    errors['login'] = "Username or password is incorrect"
    return errors

def get_all_books():
    all_books = Book.objects.all()
    return all_books

def add_book(title , desc , user_id):
    errors = Book.objects.book_validation(title , desc)
    if len(errors)==0:
        book = Book.objects.create(title = title , desc = desc , uploaded_by = User.objects.get(id = user_id) )
        fav = book.liked_by.add(User.objects.get(id = user_id))
    return errors

def add_favourite(user_id , book_id):
    book = Book.objects.get(id = book_id)
    fav = book.liked_by.add(User.objects.get(id = user_id))

def get_book(book_id):
    book = Book.objects.get(id = book_id)
    return book

def update(book_id , desc):
    book = get_book(book_id)
    book.desc = desc
    book.save()

def delete(book_id):
    book = get_book(book_id)
    book.delete()

def unfollow(user_id , book_id):
    book = get_book(book_id)
    fav = book.liked_by.remove(User.objects.get(id = user_id))
