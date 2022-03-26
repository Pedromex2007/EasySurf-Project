from unicodedata import name
from . import views
from django.urls import path, include
from .views import SurveyListView, SurveyDetailView

from easysurfQuestionnaire.views import (
    home,
)

urlpatterns = [
    path('', home, name='surveys-home')
]