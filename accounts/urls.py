from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    #path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('createUser', views.createUser),
    
]