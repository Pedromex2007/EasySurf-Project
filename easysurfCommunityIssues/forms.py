from django.forms import ModelForm
from .models import Issue, IssueReply
from django import forms

class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReplyIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
