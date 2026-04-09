from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Project, Task
class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Insert your username')
    email = forms.EmailField(label='Enter your email')
    password1 = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-type your password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Insert your username')
    password = forms.CharField(label='Insert your password', widget=forms.PasswordInput)


class ProjectCreationForm(forms.ModelForm):
  
    class Meta:
        model = Project
        fields = ['name', 'description']
    

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'assigned_to']
