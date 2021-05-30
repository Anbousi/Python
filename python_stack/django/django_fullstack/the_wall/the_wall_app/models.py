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

        #to check the age if it is > 13 years
        time_now = datetime.now()
        user_birth = datetime.strptime(post_data['birthday'], '%Y-%m-%d')
        years13 = abs((time_now-user_birth).days)
        if years13 < 4745:
            errors['birthday'] = "Age should be at least 13 years"
        
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    objects = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User,related_name='messages' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,related_name='users' , on_delete=models.CASCADE)
    message = models.ForeignKey(Messages,related_name='comments' , on_delete=models.CASCADE)
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

        User.objects.create(first_name = data['f_name'] , last_name = data['l_name'] , email = data['email'] , password = pw , birthday = data['birthday'])    
    return errors

def get_user(user):
    this_user = User.objects.filter(email = user)
    return this_user

def get_this_user(user):
    this_user = User.objects.get(email = user)
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

def p_message(id,post):
    Messages.objects.create(message = post , user = User.objects.get(id = id))

def get_messages(email):
    user = get_this_user(email)
    user_messages = user.messages.all()
    return user_messages

def get_all_messages():
    all_messages = Messages.objects.all()
