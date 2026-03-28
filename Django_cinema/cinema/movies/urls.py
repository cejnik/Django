from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('movies/<slug:slug>/', views.movie_detail, name='movie_detail'),
]
