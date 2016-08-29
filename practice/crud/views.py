from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'crud/index.html', {})


def add(request):
    return render(request, 'crud/edit.html', {})


def edit(request, editing_id):
    return render(request, 'crud/edit.html', {})


def delete(request):
    return HttpResponse('Delete')


def register(request):

    return render(request, 'crud/register.html', {})


def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    newuser = User.objects.create_user(username, None, password)
    #newuser = User.objects.create_user(username=username, password=password)
    newuser.is_active = True
    newuser.save()
    messages.success(request, '登録完了!')
    return redirect('crud:index')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('crud:home')
        else:
            messages.error(request, '入力情報に誤りがあります!')
            # return redirect('crud:index')
    else:
        # messages.error(request, '入力情報が不正です!')
        return redirect('crud:index')



def home(request):
    return render_to_response('crud/home.html')


def logout(request):
    return render(request, 'crud/logged_out.html')
