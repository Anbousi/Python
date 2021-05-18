from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('process_money', views.gold),
    path('win' , views.win),
    path('reset' , views.reset)
]