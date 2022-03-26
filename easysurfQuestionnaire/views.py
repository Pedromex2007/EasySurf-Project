from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    ListView, 
    DetailView,
)

from .models import Survey, Answer, Question
from django.http import HttpResponseRedirect


class SurveyListView(ListView):
    model = Survey
    template_name = 'easysurfQuestionnaire/index.html'
    context_object_name = 'surveys'

class SurveyDetailView(DetailView):
    model = Survey

    def get_context_data(self, **kwargs):
        

        ctx = super(SurveyDetailView, self).get_context_data(**kwargs)
        ctx['questions'] = Question.objects.all().filter(survey = self.get_object())
 
        return ctx


# Create your views here.
def home(request):
    context = {
        'surveys': Survey.objects.all()
    }
    return render(request, 'easysurfQuestionnaire/home.html', context)