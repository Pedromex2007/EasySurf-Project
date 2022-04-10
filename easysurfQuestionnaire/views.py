from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView,
)

from .models import Survey, Answer, Question
from django.http import HttpResponseRedirect

class SurveyListView(LoginRequiredMixin, ListView):
    model = Survey
    login_url = 'login'
    template_name = 'easysurfQuestionnaire/index.html'
    context_object_name = 'surveys'

class SurveyDetailView(LoginRequiredMixin,DetailView):
    model = Survey
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect('../')

    def get_context_data(self, **kwargs):
        

        ctx = super(SurveyDetailView, self).get_context_data(**kwargs)
        ctx['questions'] = Question.objects.all().filter(survey = self.get_object())
 
        return ctx


@login_required
def home(request):
    context = {
        'surveys': Survey.objects.all()
    }
    return render(request, 'easysurfQuestionnaire/home.html', context)