from django.urls import path 
from . import views # the . means the file views is located in the same directory
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new' , views.new),
    path('blogs/creat' , views.creat),
    path('blogs/<int:number>' , views.show),
    path('blogs/<int:number>/edit' , views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json' , views.json)
]