from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class CreateUser(User):
#     user = models.CharField(max_length=20)


class Report(models.Model):
    report_author = models.CharField('投稿者', max_length=20)
    report_title = models.CharField(max_length=50)
    report_content = models.CharField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_author = models.CharField(max_length=30)
    comment = models.CharField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
