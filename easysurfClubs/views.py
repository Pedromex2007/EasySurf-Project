from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    ListView, 
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Club
from django.http import HttpResponseRedirect


class ClubListView(LoginRequiredMixin, ListView):
    '''Renders all the clubs that have been registered. Users can select a specific club to join.'''
    model = Club

    login_url = 'login'

    template_name = 'easysurfClubs/index.html'
    context_object_name = 'clubs'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        print("loo")
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        print("poo")
        return render(request, self.template_name, context)

class ClubDetailView(LoginRequiredMixin, DetailView):
    '''Renders the selected club along with the button to join. Users that are not logged in will be redirected to the home page.'''
    model = Club
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        '''Override default POST function. Sets the active club for a user when they press the button.'''
        current_user = request.user

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        current_user.active_club = self.get_object()
        current_user.save()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        

        ctx = super().get_context_data(**kwargs)
        ctx['clubs'] = self.get_object()
 
        return ctx
