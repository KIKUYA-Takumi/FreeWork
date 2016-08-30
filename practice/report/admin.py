from django.contrib import admin

from .models import Report, Comment

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_author', 'report_title', 'report_content', 'created_at', 'updated_at',)

admin.site.register(Report, ReportAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_author', 'comment', 'updated_at')

admin.site.register(Comment, CommentAdmin)