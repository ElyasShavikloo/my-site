from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=37, widget=forms.TextInput(attrs={'class': 'input-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-group'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError('your entered password or username is wrong!', code='invalid_info')
