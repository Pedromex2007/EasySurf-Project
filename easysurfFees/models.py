from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
import random

class Invoice(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date_generated = models.DateTimeField(default=timezone.now)
    date_due = models.DateTimeField(default=NULL, blank=True, null=True)
    
    balance = models.FloatField(default=0.00)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title