from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
import random

class Issue(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    date_posted = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="original_poster")

    assignee = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name="issue_resolver")
    resolved = models.BooleanField(default=False)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ['date_posted']

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes

class IssueReply(models.Model):
    content = models.CharField(max_length=500)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.content

class Voter(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    has_upvoted = models.BooleanField()