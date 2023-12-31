from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': '',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '',
    }))