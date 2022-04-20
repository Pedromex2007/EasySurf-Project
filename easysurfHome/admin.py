from django.contrib import admin
from .models import Visitor
from django.contrib.auth.admin import UserAdmin


admin.site.register(Visitor)