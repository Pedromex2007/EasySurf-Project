from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (
    TemplateView
)

from account.models import ResidentChecklist

class HomePageView(TemplateView):
    template_name = 'easysurfHome/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'easysurf-home'
    template_name = 'easysurfHome/dashboard.html'
    redirect_field_name =  template_name

class ChecklistView(LoginRequiredMixin, TemplateView):
    login_url = 'easysurf-home'
    template_name = 'easysurfHome/registration-checklist.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context['done_personal_info'] = False
        context['orientation'] = False
        context['completed_survey'] = False
        context['joined_club'] = False
        context['voted_issue'] = False

        if ResidentChecklist.objects.filter(resident_id=request.user.id).exists():
            current_resident = ResidentChecklist.objects.filter(resident_id=request.user.id).first()
            print("A RESIDENT WAS FOUND WEEEEE")
            context['done_personal_info'] = current_resident.confirmed_personal_info
            context['orientation'] = current_resident.orientation
            context['completed_survey'] = current_resident.completed_survey
            context['joined_club'] = current_resident.joined_club
            context['voted_issue'] = current_resident.voted_issue


        return self.render_to_response(context)

    #def get_context_data(self, **kwargs):
    #    context = super(ChecklistView, self).get_context_data(**kwargs)
    #    context.update({'var1': self.var1, 'var2': self.var2})
    #    return context