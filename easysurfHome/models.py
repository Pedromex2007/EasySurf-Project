from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone

class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)

    resident = models.ForeignKey(Account, on_delete=models.CASCADE)

class ResidentChecklist(models.Model):
    resident = models.ForeignKey(Account, on_delete=models.CASCADE)

    confirmed_personal_info = models.BooleanField(default=False)
    orientation = models.BooleanField(default=False)
    completed_survey = models.BooleanField(default=False)
    joined_club = models.BooleanField(default=False)
    voted_issue = models.BooleanField(default=False)

class OrientationResidentDate(models.Model):
    resident = models.ForeignKey(Account, on_delete=models.CASCADE)
    orientation_date = models.DateTimeField(default=None, blank=True, null=True)
