from unicodedata import name
from django.urls import path, include
from .views import InvoiceListView, InvoiceDetailView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='fees-base'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='fees-detail'),
]