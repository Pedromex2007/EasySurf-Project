from django.forms import ModelForm
from .models import Visitor

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['first_name', 'last_name', 'phone_number']
