from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProjectCreationForm, TaskCreationForm
from django.contrib.auth.decorators import login_required
from .models import Project, Task

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

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk = pk, created_by=request.user)
    tasks = Task.objects.filter(project=project)


    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'tasks':tasks
    })

@login_required
def task(request, project_id):
    project= get_object_or_404(Project, pk = project_id, created_by = request.user)
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = Task(
                project = project,
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                status = form.cleaned_data['status'],
                priority = form.cleaned_data['priority'],
                created_by = request.user,
                assigned_to = form.cleaned_data['assigned_to']              
            )
            task.save()
            return redirect('project_detail_url', project.pk )

    else:
        form = TaskCreationForm()
    return render(request, 'tasks/task_creation.html', {
        'form': form
    })

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by = request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    else:
        return render(request, 'tasks/delete_project.html', {
            'project': project
        })
        
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk = pk, created_by= request.user)
    project= task.project
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail_url', project.pk)
    else:
        return render(request, 'tasks/delete_task.html', {
            'task': task
        })

