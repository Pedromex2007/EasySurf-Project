from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
import random

class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(default=NULL, blank=True, null=True)

    poster = models.ForeignKey(Account, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(Account)
