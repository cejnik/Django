from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='startpage'),
    path('all_movies/', views.all_movies, name='all_movies' ),
    path('all_movies/<slug:slug>', views.detail, name='movie_detail')
]
