from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView
from . forms import CustomLoginForm

urlpatterns = [
    path('', views.index, name='homepage_url'),
    path('register', views.register, name='register_url'),
    path('login/', auth_views.LoginView.as_view(template_name='bookapp/login.html', authentication_form = CustomLoginForm ), name='login_url' ),
    #path('login/', auth_views.LoginView.as_view(template_name='bookapp/login.html'), name='login_url' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('dashboard/', views.dashboard, name='dashboard_url'),
    path('protectedpage/', views.protected_page, name='protected_page_url')

]
