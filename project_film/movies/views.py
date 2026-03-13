from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
# from django.template.loader import render_to_string


#all_movies_string
#all_movie_number

movies_list = {
    'harrypotter':'Harry Potter je ...',
    'mortalcombat':'Mortal Combat je....',
    'mentalista':'Mentalista je ...',
    'suicide squad': None,
}

def index (request):
    movies_names = list(movies_list.keys())
    return render(request, 'movies/index.html', {
        'movie_names': movies_names
    })


def all_movies_string(request, movie_string):
    try:
        # movie_info = movies_list[movie_string]
        # response_data = render_to_string('movies/movie.html')     
        # return HttpResponse(response_data)
        return render(request, 'movies/movie.html',{
            'mytext': 'Martin Chejn',
            'movie_name': movie_string,
            'movie_desc': movies_list[movie_string],

        })
    except:
        return HttpResponseNotFound('Film není v databázi')
    
def all_movie_number(request, movie_number):
    movies_names_list = list(movies_list.keys())
    if movie_number > len(movies_names_list):
        return HttpResponseNotFound('Film nebyl nalezen')
    
    current_movie = movies_names_list[movie_number-1]
    return redirect('movie_url', current_movie)



