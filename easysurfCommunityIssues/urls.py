from unicodedata import name
from django.urls import path, include
from .views import IssueCreateView, IssueDetailView, IssueListView

urlpatterns = [
    path('create/', IssueCreateView.as_view(), name='issues-list'),
    path('', IssueListView.as_view(), name='issues-list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issues-issuedetail'),
]