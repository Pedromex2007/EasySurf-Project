from django.forms import ModelForm
from .models import Event
from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'content', 'event_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'event_date': DateInput(),
        }

