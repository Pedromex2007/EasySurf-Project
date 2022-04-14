from django.forms import ModelForm
from .models import Club
from django import forms

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'desc', 'location', 'meet_times', 'club_portrait']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'meet_times': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

