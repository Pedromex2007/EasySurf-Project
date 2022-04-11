from django.contrib import admin
from .models import Survey, Question, Answer
from django.contrib.auth.admin import UserAdmin

class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    filter_horizontal = ('surveyees',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(Answer)
