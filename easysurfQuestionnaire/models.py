from django.db import models
from django.contrib.auth.models import User
from account.models import Account
import random

class Survey(models.Model):
    '''Base survey model. Will have a name and description to be shown.'''
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_questions = models.IntegerField(default=1)

    surveyees = models.ManyToManyField(Account, blank=True)
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
class Question(models.Model):
    '''Base question model. Can be assigned to a survey, making it show up under that survey's detail view.'''
    content = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    
class Answer(models.Model):
    '''Answer model. To be attached to a question so questions can have dynamic answer choices. Currently not used.'''
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}"
        
    def get_answer_votes(self):
        return self.votes

#class Surveyee(models.Model):
#    user = models.ForeignKey(Account, on_delete=models.CASCADE)
#    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    