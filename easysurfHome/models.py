from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
import random

class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)

    resident = models.ForeignKey(Account, on_delete=models.CASCADE)