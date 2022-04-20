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

class InvoiceDetailView(LoginRequiredMixin, DetailView):
    '''Users that are not logged in will be redirected to the home page.'''
    model = Invoice
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        '''Override default POST function.'''

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        current_invoice = self.get_object()
        current_invoice.paid = True
        current_invoice.save()

        return HttpResponseRedirect("../")


