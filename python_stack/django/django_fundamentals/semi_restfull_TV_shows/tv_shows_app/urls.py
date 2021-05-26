from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main),
    path('new', views.new),
    path("<int:id>/edit" , views.edit ),
    path('<int:id>', views.show_this),
    path('add' , views.create),
    path('delete/<int:id>' , views.delete),
    path('<int:id>/update' , views.update)
]
