from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main),
    path('add_book', views.add_book),
    path('book/<int:id>' , views.book_show),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.authors_show),
    path('authors/select_book', views.select_book),
    path('book/select_author' , views.select_author),
]