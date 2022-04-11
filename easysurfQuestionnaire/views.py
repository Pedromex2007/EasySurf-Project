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
    #context_object_name = 'surveys'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        adjusted_surveys = Survey.objects.exclude(surveyees = request.user).count()
        print("COUNT" + str(adjusted_surveys))

        return render(request, self.template_name, context)

    def get_context_data(self, request, **kwargs):
        
        adjusted_surveys = Survey.objects.exclude(surveyees = request.user).count
        print(adjusted_surveys)
        ctx = super(SurveyDetailView, self).get_context_data(**kwargs)



        ctx['surveys'] = Question.objects.all().filter(survey = self.get_object())
 
        return ctx

class SurveyDetailView(LoginRequiredMixin, DetailView):
    model = Survey
    login_url = 'login'


    def get(self, request, *args, **kwargs):
        #if Surveyee.objects.filter(survey_id=self.get_object().pk, user_id=request.user.id).exists():
        #    return HttpResponseRedirect('../')

        if request.user in self.get_object().surveyees.all():
            return HttpResponseRedirect('../')

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        current_user = request.user

        self.object = self.get_object()

        crnt_survey = self.object
        crnt_survey.surveyees.add(current_user)
        crnt_survey.save()

        #crntSurvey = self.get_object()
        #v = Surveyee(user=request.user, survey=crntSurvey)
        #v.save()

        return HttpResponseRedirect('../')

    def get_context_data(self, **kwargs):
        

        ctx = super(SurveyDetailView, self).get_context_data(**kwargs)
        ctx['questions'] = Question.objects.all().filter(survey = self.get_object())
 
        return ctx


@login_required
def home(request):
    context = {
        'surveys': Survey.objects.exclude(surveyees = request.user)
    }
    return render(request, 'easysurfQuestionnaire/home.html', context)