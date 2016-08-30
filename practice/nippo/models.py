from django.db import models

# Create your models here.


class Report(models.Model):
    report_author = models.CharField(max_length=30)
    report_title = models.CharField(max_length=50)
    report_content = models.CharField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_author = models.CharField(max_length=30)
    comment = models.CharField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
