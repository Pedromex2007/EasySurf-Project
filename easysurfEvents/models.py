from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(default=None, blank=True, null=True)

    poster = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="event_op")
    subscribers = models.ManyToManyField(Account, blank=True, related_name="event_subbers")

    def __str__(self):
        return self.title