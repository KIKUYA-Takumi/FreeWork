from django.shortcuts import render, redirect, render_to_response, get_list_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Report, Comment, Author
from .forms import ReportForm, CommentForm, SearchForm, UserCreationForm


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
            search_words = form.cleaned_data['search_word'].split()
            search_reports = []
            for i in range(len(search_words)):
                search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
            return render_to_response(
                'report/search.html',
                {'form': form, 'reports': search_reports},
                RequestContext(request)
            )

        return render(request, 'report/search.html', {'form': form})


def report_browse(request, report_id=None):
    if report_id:
        report = get_object_or_404(Report, pk=report_id)
    else:
        report = Report()

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report.save()
            return redirect('report:index')
    else:
        form = ReportForm(instance=report)
    return render(request, 'report/browse.html', {'form': form, 'report_id': report_id})


def edit_report(request, report_id):

    return render(request, 'report/edit.html', {})


class AuthorCreate(CreateView):
    model = Author
    form = UserCreationForm
    template_name = 'user_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('report:user_creation')


class ReportIndex(ListView):
    model = Report
    template_name = 'report/index.html'


class ReportDetail(DetailView):
    model = Report
    template_name = 'report/detail.html'




