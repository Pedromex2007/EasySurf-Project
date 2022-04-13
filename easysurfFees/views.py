from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    ListView, 
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Invoice
from django.http import HttpResponseRedirect

class InvoiceListView(LoginRequiredMixin, ListView):
    '''This view lists out all the active fees.'''
    model = Invoice
    login_url = 'login'
    template_name = 'easysurfFees/fees.html'
    context_object_name = 'invoices'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

