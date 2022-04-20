from django.forms import ModelForm
from .models import Visitor
from django import forms

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ('first_name', 'last_name', 'phone_number', 'visitor_relationship', 'visitor_portrait')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            #'visitor_relationship': forms.TextInput(attrs={'class': 'form-control'}),
            #'visitor_portrait': forms.TextInput(attrs={'class': 'form-control'}),
        }
