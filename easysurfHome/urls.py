from unicodedata import name
from . import views
from django.urls import path, include
from .views import HomePageView, DashboardView, ChecklistView, OrientationView, VisitorListView, VisitorCreateView

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
    path('dashboard', DashboardView.as_view(), name = 'home-dashboard'),
    path('checklist', ChecklistView.as_view(), name = 'home-checklist'),
    path('orientation', OrientationView.as_view(), name = 'home-orientation'),
    path('visitors', VisitorListView.as_view(), name = 'visitors-list'),
    path('visitors/create', VisitorCreateView.as_view(), name='visitors-create'),
]