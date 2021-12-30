from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from my_board.models import board
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    # DB의 board 테이블의 모든 내용을 가져온다
    rows = board.objects.all()
    content = {'rows':rows}
    return render(request, 'my_board/list.html', content)
    #return HttpResponse('연결이 완료됨')


def index1(request):
    return render(request, 'my_board/login.html')
def index2(request):
    return render(request, 'my_board/write.html')
def content(request):
    return render(request, 'my_board/content.html')
def create(request):
    # return HttpResponse('게시글을 생성합니다')
    # user_input_str = request.POST['createDate']
    # return HttpResponse(f'사용자가 입력한 값:{user_input_str}')
    #createDate = request.POST['createDate']
    #writer = request.POST['user']
    #subject = request.POST['subject']
    #content = request.POST['content']
    new = board(
        createDate=request.POST['createDate'], 
        writer=request.POST['user'], 
        subject=request.POST['subject'], 
        content=request.POST['content'],
    )
    new.save()

    return HttpResponseRedirect(reverse('list'))

def delete( request ):
  #print( request.GET[''])
  old = board.objects.get(id= request.GET['id'])
  old.delete()
  return HttpResponseRedirect(reverse('list'))
  

def update( request ):
    #print('id:', request.GET['id'])
    post = board.objects.get(id=request.GET['id'])
    content = {'post':post}
    return render( request, 'my_board/update.html', content)

def modify( request ):
    post = board.objects.get(id=request.POST['id'])
    post.createDate = request.POST['createDate']
    post.writer=request.POST['user']
    post.subject=request.POST['subject'] 
    post.content=request.POST['content']
    post.save()
    return HttpResponseRedirect(reverse('list'))

def view(request):
    post = board.objects.get(id=request.GET['id'])
    content = {'post':post}
    return render(request, 'my_board/view.html', content)

