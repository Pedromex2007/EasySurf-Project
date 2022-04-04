from asyncio.windows_events import NULL
from multiprocessing import context
from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    ListView, 
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from django.http import HttpResponseRedirect

class EventListView(LoginRequiredMixin, ListView):
    '''This view lists out all the active events.'''
    model = Event
    login_url = 'easysurf-home'
    template_name = 'easysurfEvents/index.html'
    context_object_name = 'events'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if request.POST.get(str(2)):
            print("JOINED THIS CLUB")
        return render(request, self.template_name, context)

class EventDetailView(LoginRequiredMixin, DetailView):
    '''View to render an event's details.'''
    model = Event
    login_url = 'easysurf-home'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        crnt_event = self.object

        if request.user in crnt_event.subscribers.all():
            print("Uesr is subscriber")
            #TODO: Extra stuff like changing the buttons if the user is already subscribed to this event.

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        current_user = request.user

        self.object = self.get_object()

        crnt_event = self.object
        crnt_event.subscribers.add(current_user)
        crnt_event.save()

        if request.POST.get("event_sub"):
            return HttpResponseRedirect('../')

    def get_context_data(self, **kwargs):    
        ctx = super(EventDetailView, self).get_context_data(**kwargs)
        return ctx
