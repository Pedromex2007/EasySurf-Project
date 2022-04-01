from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    model = Event
    filter_horizontal = ('subscribers',)

admin.site.register(Event, EventAdmin)