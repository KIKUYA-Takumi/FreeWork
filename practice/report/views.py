from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Report, Comment
from .forms import ReportForm, CommentForm


# Create your views here.


def index(request):
    reports = Report.objects.all().order_by('-id')
    return render(request, 'report/index.html', {'reports': reports})


def entries(request):
    return render(request, 'report/entry.html')


def create_report(request):
    form = ReportForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '投稿を受け付けました!')
            return redirect('report:index')
        else:
            messages.error(request, '入力内容に誤りがあります!')
    return render(request, 'report/index.html')


