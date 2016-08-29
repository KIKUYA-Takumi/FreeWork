from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'crud/index.html')


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
    newuser.save()
    messages.success(request, '登録完了!')
    return redirect('crud/index.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('crud/home.html')
        else:
            return redirect('crud/index.html')
    else:
        return redirect('crud/index.html')


def home(request):
    return render_to_response('crud/home.html')

