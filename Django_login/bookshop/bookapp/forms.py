from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Uživatelské jméno: ')
    email = forms.EmailField(label='Email: ')
    password1 = forms.CharField(label='Heslo: ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potvrďte heslo: ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Uživatelské jméno')
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)