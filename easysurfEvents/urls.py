from django.urls import path, include
from .views import EventListView, EventDetailView, EventCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('create', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-eventdetail'),
]