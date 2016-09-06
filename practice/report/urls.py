from django.conf.urls import url
from . import views
from .views import AuthorCreate, ReportList, ReportDetail, ReportEdition, ReportDelete


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^report_entries/', views.create_report, name='create_report'),
    url(r'^entries/', views.entries, name='entries'),
    url(r'^search/', views.search, name='search'),
    url(r'^edition/', views.edit_report, name='edition'),
    url(r'^user_creation/', AuthorCreate.as_view(), name='user_creation'),
    url(r'^report_list/', ReportList.as_view(), name='report_list'),
    url(r'^(?P<pk>[0-9]+)/$', ReportDetail.as_view(), name='report_detail'),
    url(r'^(?P<pk>[0-9]+)/edition/$', ReportEdition.as_view(), name='report_edition'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ReportDelete.as_view(), name='report_delete'),
]
