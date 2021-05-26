from django.db import models
from django.db.models.fields import TimeField

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def show_tv():
    show_tv = Shows.objects.all()
    return show_tv

def create_show(postdata):
    u = Shows.objects.create(title=postdata['title'], network=postdata['network'],release_date=postdata['release_date'] , description=postdata['description'] )
    return u

def delete_this(postdata):
    Shows.objects.get(id = postdata).delete()

def edit_this(id):
    update_show = Shows.objects.get(id=id)
    return update_show