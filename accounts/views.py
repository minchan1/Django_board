from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from my_board.models import board
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')


def createUser(request):
    id = request.POST['id']
    pw = request.POST['pw']
    user = User(username=id, password=make_password(pw))
    user.save()
    return HttpResponseRedirect(reverse('list'))