from django import forms
from .models import  Report, Comment


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_title', 'report_content')
        widget = {
            'report_title': forms.TextInput(attrs={'size' : 50}),
            'report_content': forms.Textarea(attrs={'cols': 40, 'rows': 25})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widget = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 25})
        }