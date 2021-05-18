from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main),
    path('guess_num' , views.guess_num) ,
    path('calculations' , views.calculations),
    path('reset', views.reset),
    path('win', views.win)

]