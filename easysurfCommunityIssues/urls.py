from unicodedata import name
from django.urls import path, include
from .views import IssueCreateView, IssueDetailView, IssueListView, IssueEditView

urlpatterns = [
    path('create/', IssueCreateView.as_view(), name='issues-list'),
    path('', IssueListView.as_view(), name='issues-list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issues-issuedetail'),
    path('edit/<int:pk>/', IssueEditView.as_view(), name='update-issue'),
]