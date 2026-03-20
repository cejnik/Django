from django.shortcuts import render
from movies.models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',{
        'movies': movies,
    })