from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Report, Comment
from .forms import ReportForm, CommentForm


# Create your views here.


def index(request):
    return render(request, 'nippo/index.html', {})
