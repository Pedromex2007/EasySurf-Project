from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)

    class Relationship(models.TextChoices):
        SON = 'SO', _('Son')
        DAUGHTER = 'DA', _('Daughter')
        GRANDSON = 'GS', _('Grandson')
        GRANDDAUGHTER = 'GD', _('Granddaughter')
        BROTHER = 'BR', _('Brother')
        SISTER = 'SI', _('Sister')

    visitor_relationship = models.CharField(
        max_length=2,
        choices=Relationship.choices,
        default=Relationship.SON,
    )

    visitor_portrait = models.ImageField(default=None, null=True, upload_to="images/")

    resident = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def get_relationship(self):
        return self.Relationship(self.visitor_relationship).label

class OrientationResidentDate(models.Model):
    resident = models.ForeignKey(Account, on_delete=models.CASCADE)
    orientation_date = models.DateTimeField(default=None, blank=True, null=True)
