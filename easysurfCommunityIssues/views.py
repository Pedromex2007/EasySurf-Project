from multiprocessing import context
from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    ListView, 
    DetailView,
    TemplateView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Issue, IssueReply
from .forms import CreateIssueForm, ReplyIssueForm
from django.http import HttpResponseRedirect

class IssueListView(ListView):
    model = Issue
    template_name = 'easysurfCommunityIssues/index.html'
    context_object_name = 'issues'

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

class IssueDetailView(DetailView):
    model = Issue

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print("Getting!")
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        replyPost = ReplyIssueForm(self.request.POST or None)
        if replyPost.is_valid():
            print(self.get_object)
            replyPost.instance.issue = self.get_object()
            replyPost.save()
            return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        issueReply = ReplyIssueForm(self.request.POST or None)
        


        ctx = super(IssueDetailView, self).get_context_data(**kwargs)
        ctx['responses'] = IssueReply.objects.all().filter(issue = self.get_object())
        ctx['form'] = issueReply
        return ctx

class IssueCreateView(CreateView):
    '''View to create issue form fields automatically in the desinated template. Users should be logged in to access this page.'''
    form_class = CreateIssueForm
    template_name = 'easysurfCommunityIssues/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'


def create(request):

    if(request.method == 'POST'):
        form = CreateIssueForm(request.POST)
        if(form.is_valid()):
            form.user = request.user
            form.save()
            return redirect('easysurf-home')
    else:
        form = CreateIssueForm

    context = {
        'form': form
    }
    return render(request, 'easysurfCommunityIssues/create.html', context)