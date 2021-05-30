from favourite_books.settings import DATABASES
from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_reg),
    path('books/' , views.home),
    path('login_registration/', views.check),
    path('logout/', views.logout),
    path('books/add_book' , views.add_book),
    path('books/add_favourite/<int:book_id>' , views.add_favourite),
    path('books/<int:book_id>/' , views.view_book),
    path('books/update/<int:book_id>' , views.update),
    path('books/delete/<int:book_id>' , views.delete),
    path('books/unfollow/<int:book_id>' , views.unfollow),
]