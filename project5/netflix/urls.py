from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('movies', views.all_movies_page, name='movies_page')

]