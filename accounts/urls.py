from django.urls import path
from django.urls.conf import include

from . import views
from my_board import views as board_views   
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.index),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', views.signup),
    path('createUser', views.createUser),
    path('profile/', board_views.index),
    
]