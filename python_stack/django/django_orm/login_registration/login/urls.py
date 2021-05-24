from login import views
from django.urls import path
urlpatterns= [
    path('',views.main),
    path('login', views.login)
]