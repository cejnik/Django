from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='starting_page'),
    path('all_movies/', views.all_movies, name='all_movies_page'),
    path('all_movies/<slug:slug>', views.movie_detail, name='movie_detail_page')
]
