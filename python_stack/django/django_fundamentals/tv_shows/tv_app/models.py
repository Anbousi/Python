from django.contrib.messages.api import error
from django.core.checks import messages
from django.db import models
from django.http import request
from django.shortcuts import redirect
# Create your models here.

class ShowsManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}
        if len(post_data['title']) < 2:
            errors['title'] = "Title should be at least 2 Chars."
        
        if len(post_data['network']) < 3:
            errors['network'] = "Network should be at least 3 Chars."
        
        if len(post_data['description']) < 10:
            errors['description'] = "Description should be at least 10 Chars."
        
        return errors
        
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    objects = ShowsManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def read_shows():
    all_shows = Shows.objects.all()
    return  all_shows

def create_show(data):
    new_show = Shows.objects.create(title = data['title'], network = data['network'] , description = data['description'], release_date = data['release_date'])
    return new_show

def this_show(id):
    this_show = Shows.objects.get(id = id)
    return this_show

def delete_this(id):
    this_show = Shows.objects.get(id = id)
    this_show.delete()
    
# def edit_this(id):
#     this_show = Shows.objects.get(id = id)
#     this_show.title

def update_show(data):
    this_show = Shows.objects.get(id=data['id'])
    this_show.title = data['title']
    this_show.network = data['network']
    this_show.description = data['description']
    this_show.release_date = data['release_date']
    messages.success(request,'Show successfully updated')
    this_show.save()