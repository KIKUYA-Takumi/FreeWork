from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.


def register(request):
    # username = request.POST['username']
    return render(request, 'nippo/login.html', {})


def index(request):
    return render(request, 'nippo/login.html', {})
