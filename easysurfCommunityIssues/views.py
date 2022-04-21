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
from account.models import ResidentChecklist
from django.urls import reverse

class IssueListView(LoginRequiredMixin, ListView):
    '''This view lists out all the issues all users have posted. Users can click on an issue to see all the responses and also agree/disagree with the post.'''
    model = Issue
    login_url = 'login'
    template_name = 'easysurfCommunityIssues/index.html'
    context_object_name = 'issues'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

class IssueDetailView(LoginRequiredMixin, DetailView):
    '''View to render a specific issue's replies and upvotes/downvotes. This also controls the logic behind the reply form and the downvote/upvote button.'''
    model = Issue
    login_url = 'login'

    def vote(self, request, issue_id, upvoted):
        '''Downvote or upvote a master post. User can switch their vote.'''

        if ResidentChecklist.objects.filter(resident_id=request.user.id).exists():
            current_resident = ResidentChecklist.objects.filter(resident_id=request.user.id).first()
            current_resident.voted_issue = True
            current_resident.save()
        else:
            user_checklist = ResidentChecklist(resident = request.user)
            user_checklist.voted_issue = True
            user_checklist.save()

        crntIssue = self.get_object()

        if Voter.objects.filter(issue_id=issue_id, user_id=request.user.id).exists():
            current_voter = Voter.objects.filter(issue_id=issue_id, user_id=request.user.id).first()

            if(current_voter.has_upvoted and upvoted):
                #Do nothing.
                pass
            elif(current_voter.has_upvoted and not upvoted):
                print("Change to DOWNVOTING")
                crntIssue.upvotes -= 1
                crntIssue.downvotes += 1
                crntIssue.save()
                current_voter.has_upvoted = False
                current_voter.save()
            elif(not current_voter.has_upvoted and upvoted):
                print("Change to UPVOTE")
                crntIssue.upvotes += 1
                crntIssue.downvotes -= 1
                crntIssue.save()
                current_voter.has_upvoted = True
                current_voter.save()
            else:
                print("Different conditional")

            print(current_voter.issue)
            print("Already voted.")
        else:
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
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        replyPost = ReplyIssueForm(self.request.POST or None)

        if replyPost.is_valid():

            reply = IssueReply(content=replyPost.instance.content, user=request.user, issue=self.get_object())
            reply.save()

            return HttpResponseRedirect(self.request.path_info)
        else:
            if request.POST.get("upvote_btn"):
                self.vote(request, self.get_object().pk, True)
                print("UPVOTE")
                return HttpResponseRedirect(self.request.path_info)
            elif request.POST.get("downvote_btn"):
                self.vote(request, self.get_object().pk, False)
                print("DOWNVOTE")
                return HttpResponseRedirect(self.request.path_info)
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
        return '../../'
