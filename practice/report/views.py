from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.db.models import Q

from .models import Report, Comment
from .forms import ReportForm, CommentForm, SearchForm


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
            return render(request, 'report/index.html', {'form': form})
        else:
            messages.error(request, '入力内容に誤りがあります!')
    return render(request, 'report/entry.html', {'form': form})


def search(request):
    form = SearchForm(request.GET or None)
    if request.method == 'GET':
        if form.is_valid():
            reports = Report.objects.filter(Q(report_content__contains=form.cleaned_data['search_word']))
            return render_to_response('report/search.html', {'form': form, 'reports': reports}, RequestContext(request))
    else:
        return render(request, 'report/search.html', {'form': form})



