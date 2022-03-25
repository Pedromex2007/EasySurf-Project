from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


class AccountAuthenticationForm(forms.ModelForm):
    '''This form will render and create the login fields.'''

    #password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'password',
                }),
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                print("ERROR INVALID LOGIN")
                raise forms.ValidationError("Invalid login.")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'phone_number', 'home_address')

    def clean_email(self):
        if(self.is_valid()):
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" already in use.' % account.email)
    def clean_username(self):
        if(self.is_valid()):
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" already in use.' % account.username)
    def clean_number(self):
        if(self.is_valid()):
            phone_number = self.cleaned_data['phone_number']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(phone_number=phone_number)
            except Account.DoesNotExist:
                return phone_number
            raise forms.ValidationError('Phone number "%s" already in use.' % account.phone_number)

    