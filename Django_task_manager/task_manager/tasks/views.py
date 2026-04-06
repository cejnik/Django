from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProjectCreationForm
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()
    return render(request, 'tasks/register.html', {
        'form': form
    })

@login_required
def dashboard(request):
    projects = Project.objects.filter(created_by = request.user)
    return render(request, 'tasks/dashboard.html', {
        'projects':projects
    })

@login_required
def createproject(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            project = Project(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                created_by = request.user,
            )
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectCreationForm()
    return render(request, 'tasks/project_creation.html', {
        'form': form
    })
