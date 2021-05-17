from django.urls import path
from . import views
urlpatterns = [
    path('',(views.index)),
    path('counter', views.counter),
    path('reset', views.reset),
    path('hard_reset', views.hard_reset),
    path('inc', views.inc)
]