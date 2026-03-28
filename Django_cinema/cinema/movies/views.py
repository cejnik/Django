from django.shortcuts import render, get_object_or_404
from . models import Film

# Create your views here.
def index(request):
    movies = Film.objects.all()
    return render(request, 'movies/index.html',{
        'movies':movies
    })

def movie_detail(request, slug):
    movie = get_object_or_404(Film, slug=slug)
    return render(request, 'movies/movie_detail.html', {
        'movie':movie
    })