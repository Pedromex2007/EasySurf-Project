from unicodedata import name
from django.urls import path, include
from .views import ClubListView, ClubDetailView

urlpatterns = [
    path('', ClubListView.as_view(), name='clubs-home'),
    path('<int:pk>/', ClubDetailView.as_view(), name='club-clubdetail'),
]