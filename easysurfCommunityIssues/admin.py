from django.contrib import admin
from .models import Issue, IssueReply, Voter

admin.site.register(Issue)
admin.site.register(IssueReply)

#The voter object should NOT be here in production deployment! This is just for debugging purposes.
admin.site.register(Voter)