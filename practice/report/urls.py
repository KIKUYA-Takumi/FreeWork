from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^report_entries', views.create_report, name='create_report'),
    url(r'^entries', views.entries, name='entries')
]
