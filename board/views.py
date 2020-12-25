from django.shortcuts import render, redirect
import json
from  django.http import HttpResponse, JsonResponse
from django.db.models import Count, Avg, Max, Min, Sum
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages


# models.py에서 만든 DB 테이블의 데이터를 처리하는 로직을 만들 수 있다.
# Create your views here.
def index(request):
    if request.method == 'GET':
        # 로그인 상태 확인
        if request.user.is_authenticated:
            return render(request, 'board/boardlist.html')
        else:
            return render(request, 'board/index.html')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pw']
        print('아이디 : '+email+', 비번 : '+password)

        user = authenticate(username=email, password=password)

        # 계정이 일치 확인
        if user is not None:
            login(request, user)
            return render(request, 'board/boardlist.html')
        else:
            return render(request, 'board/index.html')


def logout_action(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'GET':
        return render(request, 'board/signupform.html')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pw']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        nickname = request.POST['nickname']
        gender = request.POST['gender']

        # 해당 계정이 이미 존재하는지 확인하는 과정
        email_cnt = User.objects.filter(username=email).aggregate(Count('username'))
        nickname_cnt = User.objects.filter(nickname=nickname).aggregate(Count('nickname'))

        if email_cnt['username__count'] > 0:
            res = JsonResponse({'message': 0})
            return HttpResponse(res)
        elif nickname_cnt['nickname__count'] > 0:
            res = JsonResponse({'message': 1})
            return HttpResponse(res)
        else:
            res = JsonResponse({'message': 2})
            user = User.objects.create_user(username=email, password=password, last_name=last_name, first_name=first_name, gender=gender, nickname=nickname)
            user.save()
            return HttpResponse(res)


def boardlist(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'board/boardlist.html')
        else:
            return redirect('index')



