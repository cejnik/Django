from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_number>', views.all_movie_number),
    path('<str:movie_string>', views.all_movies_string, name = 'movie_url'),

]