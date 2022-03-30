from django.forms import ModelForm
from .models import Issue, IssueReply

class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'content']

class ReplyIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['content']
