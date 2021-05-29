from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_reg),
    path('home/' , views.home),
    path('login_registration/', views.check),
    path('logout', views.logout)
]
