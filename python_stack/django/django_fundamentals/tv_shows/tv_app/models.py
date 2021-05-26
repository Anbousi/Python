from django.db import models
from django.shortcuts import redirect
# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
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
    
def edit_this(id):
    this_show = Shows.objects.get(id = id)
    this_show.title

def update_show(data):
    this_show = Shows.objects.get(id=data['id'])
    this_show.title = data['title']
    this_show.network = data['network']
    this_show.description = data['description']
    this_show.release_date = data['release_date']
    this_show.save()