from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    ListView, 
    DetailView,
)

from .models import Club
from django.http import HttpResponseRedirect


class ClubListView(ListView):
    model = Club
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

class ClubDetailView(DetailView):
    model = Club

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print("Getting!")
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        current_user = request.user

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print("Posting!")
        current_user.active_club = self.get_object()
        current_user.save()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        

        ctx = super().get_context_data(**kwargs)
        ctx['clubs'] = self.get_object()
 
        return ctx
