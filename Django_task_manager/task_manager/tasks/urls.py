from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='tasks/index.html', authentication_form = LoginForm), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('register/', views.register, name='registration_url'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-project/', views.createproject, name='create_project_url'),
    path('project-detail/<int:pk>/', views.project_detail, name='project_detail_url'),
]
