from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from my_board.models import board
from django.urls import reverse
from django.contrib.auth.models import User
from my_board.models import board_reply

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


    # 데코레이터를 이용해서 로그인이 필요한 함수를 지정
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def create(request):

    if request.method == 'POST':
        new = board(
            user = request.user,
            createDate=request.POST['createDate'], 
            #writer=request.POST['user'], 
            subject=request.POST['subject'], 
            content=request.POST['content'],    
        )   
        new.save()

        return HttpResponseRedirect(reverse('list'))
    else :
        # 로그인이 되어있지 않은 경우 로그인 이후에 새로 글을 작성
        return render(request, 'my_board/write.html')

@login_required(login_url='/accounts/login/')
def delete( request ):
    old = board.objects.get(id= request.GET['id'])
  #print( request.GET[''])
    if request.user != old.user:
        return render(request,'my_board/alert.html')
    else:
        old.delete()
    return HttpResponseRedirect(reverse('list'))
    
@login_required(login_url='/accounts/login/')
def update( request ):
    #print('id:', request.GET['id'])
    post = board.objects.get(id=request.GET['id'])
    content = {'post':post}
    return render( request, 'my_board/update.html', content)

@login_required(login_url='/accounts/login/')
def modify( request ):
    post = board.objects.get(id=request.POST['id'])
    if request.user != post.user:
        return render(request,'my_board/alert.html')
    else:
        post.createDate = request.POST['createDate']
        post.writer=request.POST['user']
        post.subject=request.POST['subject'] 
        post.content=request.POST['content']
        post.save()
    return HttpResponseRedirect(reverse('list'))

def view(request):
    post = board.objects.get(id=request.GET['id'])
    reply1 = board_reply.objects.all()
    content = {'post':post, 'reply':reply1}   
    return render(request, 'my_board/view.html', content)


def reply(request):
    post = board_reply(
            user = request.user,
            createDate=request.POST['createDate'], 
            content=request.POST['content'],    
        )   
    post.save()

    return HttpResponseRedirect(reverse('list'))