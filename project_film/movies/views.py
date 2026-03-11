from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


#all_movies_string
#all_movie_number

movies_list = {
    'harrypotter':'Harry Potter je ...',
    'mortalcombat':'Mortal Combat je....',
    'mentalista':'Mentalista je ...',
}

def index (request):
    content = ''
    movies_names = list(movies_list.keys())
    content = '<ul>'
    for one_movie in movies_names:
        url = reverse('movie_url', args=[one_movie])
        content += f'<li><a href="{url}">{one_movie}</a></li>'
    content += '</ul>'
    return HttpResponse(content)

def all_movies_string(request, movie_string):
    try:
        movie_info = movies_list[movie_string]
        return HttpResponse(movie_info)
    except:
        return HttpResponseNotFound('Film není v databázi')
    
def all_movie_number(request, movie_number):
    movies_names_list = list(movies_list.keys())
    if movie_number > len(movies_names_list):
        return HttpResponseNotFound('Film nebyl nalezen')
    
    current_movie = movies_names_list[movie_number-1]
    return redirect('movie_url', current_movie)



