from unicodedata import name
from django.urls import path, include
from .views import InvoiceListView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='fees-base'),
    #path('<int:pk>/', ClubDetailView.as_view(), name='club-clubdetail'),
]