from unicodedata import name
from . import views
from django.urls import path, include
from .views import HomePageView

from account.views import (
    logout_view,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='easysurf-home'),
    path('logout', logout_view, name='logout'),
]