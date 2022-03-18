from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (
    TemplateView
)

class HomePageView(TemplateView):
    template_name = 'easysurfHome/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'easysurf-home'
    template_name = 'easysurfHome/dashboard.html'
    redirect_field_name =  template_name