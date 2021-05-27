from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home),
    path('books/', views.add_book_template),
    path('authors/', views.add_author_template),
    path('create_book', views.create_book),
    path('create_author', views.create_author),
    path('books/<int:id>/' , views.view_book),
    path('authors/<int:id>/' , views.view_author),
    path('books/<int:id>/add_author_to_book', views.add_author_to_book),
    path('authors/<int:id>/add_book_to_author', views.add_book_to_author),

]