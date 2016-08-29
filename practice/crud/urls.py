from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^register/', views.register, name='register'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
]