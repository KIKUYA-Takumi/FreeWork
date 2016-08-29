from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^register/', views.register, name='register'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^home/', views.login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'crud/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'crud/logged_out.html'}),
]