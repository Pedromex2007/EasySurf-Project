from multiprocessing import context
from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    ListView, 
    DetailView,
    UpdateView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Issue, IssueReply, Voter
from .forms import CreateIssueForm, ReplyIssueForm
from django.http import HttpResponseRedirect

class IssueListView(LoginRequiredMixin, ListView):
    '''This view lists out all the issues all users have posted. Users can click on an issue to see all the responses and also agree/disagree with the post.'''
    model = Issue
    login_url = 'easysurf-home'
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

class IssueDetailView(LoginRequiredMixin, DetailView):
    '''View to render a specific issue's replies and upvotes/downvotes. This also controls the logic behind the reply form and the downvote/upvote button.'''
    model = Issue
    login_url = 'easysurf-home'

    def vote(self, request, issue_id, upvoted):
        '''Downvote or upvote a master post. User can switch their vote.'''
        #TODO: Allow user to switch their vote.
        if Voter.objects.filter(issue_id=issue_id, user_id=request.user.id).exists():
            current_voter = Voter.objects.filter(issue_id=issue_id, user_id=request.user.id).first()
            print(current_voter.issue)
            print("Already voted.")
        else:
            crntIssue = self.get_object()

            if upvoted:
                crntIssue.upvotes += 1
            else:
                crntIssue.downvotes += 1

            crntIssue.save()
            v = Voter(user=request.user, issue=crntIssue, has_upvoted=upvoted)
            v.save()
            print("Object upvoted")


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print("Getting!")
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        replyPost = ReplyIssueForm(self.request.POST or None)

        if replyPost.is_valid():

            reply = IssueReply(content=replyPost.instance.content, user=request.user, issue=self.get_object())
            reply.save()

            return HttpResponseRedirect('/')
        else:
            if request.POST.get("upvote_btn"):
                self.vote(request, self.get_object().pk, True)
                print("UPVOTE")
                return HttpResponseRedirect('/')
            elif request.POST.get("downvote_btn"):
                self.vote(request, self.get_object().pk, False)
                print("DOWNVOTE")
                return HttpResponseRedirect('/')
            else:
                print("Something went horribly wrong!")


    def get_context_data(self, **kwargs):
        issueReply = ReplyIssueForm(self.request.POST or None)
        


        ctx = super(IssueDetailView, self).get_context_data(**kwargs)
        ctx['responses'] = IssueReply.objects.all().filter(issue = self.get_object())
        ctx['form'] = issueReply
        return ctx


class IssueCreateView(LoginRequiredMixin, CreateView):
    '''View to create issue form fields automatically in the desinated template. Users should be logged in to access this page.'''
    form_class = CreateIssueForm
    login_url = 'easysurf-home'
    template_name = 'easysurfCommunityIssues/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '../'

class IssueEditView(LoginRequiredMixin, UpdateView):
    model = Issue
    login_url = 'easysurf-home'
    template_name = 'easysurfCommunityIssues/edit_post.html'
    fields = ['title', 'content']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if(self.object.user.pk is not request.user.pk):
            print("Not the user.")
            return HttpResponseRedirect('../../')
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        return '../'
