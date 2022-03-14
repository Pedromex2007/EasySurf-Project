from unicodedata import name
from . import views
from django.urls import path, include
from .views import HomePageView

from account.views import (
    update_account_info,
    logout_view,
    login_view,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='easysurf-home'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('updateinfo', update_account_info, name='update-info'),
]