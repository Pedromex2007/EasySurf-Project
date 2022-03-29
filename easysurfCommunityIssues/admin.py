from django.contrib import admin
from .models import Issue, IssueReply, Voter

admin.site.register(Issue)
admin.site.register(IssueReply)