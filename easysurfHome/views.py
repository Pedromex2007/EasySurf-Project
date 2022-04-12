from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView
)

from account.models import ResidentChecklist
from .models import OrientationResidentDate

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

class OrientationView(LoginRequiredMixin, TemplateView):
    login_url = 'easysurf-home'
    template_name = 'easysurfHome/orientation-meeting.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context['submitted_orientation_date'] = False

        if OrientationResidentDate.objects.filter(resident_id=request.user.id).exists():
            current_resident = OrientationResidentDate.objects.filter(resident_id=request.user.id).first()
            context['selected_date'] = current_resident.orientation_date
            context['submitted_orientation_date'] = True


        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.POST.get("orientation-date"):

            if ResidentChecklist.objects.filter(resident_id=request.user.id).exists():
                resident_checklist = ResidentChecklist.objects.filter(resident_id=request.user.id).first()
                resident_checklist.orientation = True
                resident_checklist.save()
                
            thedate = request.POST.get("orientation-date")

            if OrientationResidentDate.objects.filter(resident_id=request.user.id).exists():
                current_resident = OrientationResidentDate.objects.filter(resident_id=request.user.id).first()
                current_resident.orientation_date = thedate
                current_resident.save()
            else:
                print("Creating new orientation date")
                new_orientation = OrientationResidentDate(resident = request.user, orientation_date = thedate)
                new_orientation.save()
            return HttpResponseRedirect(self.request.path_info)

        else:
            print("Gotta select a date!")
            #TODO: Raise an error and print to screen, but actually that's pretty hard and we ain't got time so nevermind.
            return HttpResponseRedirect(self.request.path_info)