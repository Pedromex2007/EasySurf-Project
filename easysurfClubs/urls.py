from unicodedata import name
from django.urls import path, include
from .views import ClubListView, ClubDetailView, ClubCreateView

urlpatterns = [
    path('', ClubListView.as_view(), name='clubs-home'),
    path('create', ClubCreateView.as_view(), name='clubs-create'),
    path('<int:pk>/', ClubDetailView.as_view(), name='club-clubdetail'),
]