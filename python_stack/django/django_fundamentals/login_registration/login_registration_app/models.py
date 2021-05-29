import datetime
from django.contrib.messages.api import error
from django.contrib import messages
from django.db import models
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
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    objects = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(post_data):
    errors = Users.objects.basic_validator(post_data)
    db_email = Users.objects.filter(email = data['email'])

    if db_email:
        errors['db_email'] = "This email is used."    
    
    if len(errors) == 0:
        #hash password before saving in database
        pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt()).decode()

        Users.objects.create(first_name = data['f_name'] , last_name = data['l_name'] , email = data['email'] , password = pw , birthday = data['birthday'])
    
    return errors

def get_user(user):
    this_user = Users.objects.filter(email = user)
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
