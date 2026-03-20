from django.shortcuts import render, get_object_or_404
from music.models import Music
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.

def index(request):
    musics = Music.objects.all().order_by('-rating')
    num_songs = musics.count()
    avg_rating = musics.aggregate(Avg('rating'))
    return render(request, 'music/index.html', {
        'musics': musics,
        'total_songs_number': num_songs,
        'avg_rating': avg_rating
    })

def detail(request, slug):
    # try:
    #     song = Music.objects.get(id=music_id)
    # except:
    #     raise Http404()

    song = get_object_or_404(Music,slug=slug)

    return render(request, 'music/detail.html', {
        'musics': song
    })

    