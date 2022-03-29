from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from account.models import Account
import random

class Issue(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes

class Reply(models.Model):
    content = models.CharField(max_length=500)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

class Voter(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    has_upvoted = models.BooleanField()