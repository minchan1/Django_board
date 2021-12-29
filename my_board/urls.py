from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    #path('my_board/', include('my_board')),
    #path('admin/', admin.site.urls),
    path('', views.index, name='list'),
    path('login/', views.index1),
    path('write/', views.index2),
    path('create', views.create),
    path('delete', views.delete),
    path('update/', views.update),
    path('modify/', views.modify),
]