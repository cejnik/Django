from django.shortcuts import render, get_object_or_404, redirect
from . models import Film, Screening, Reservation
from . forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Film.objects.all()
    return render(request, 'movies/index.html',{
        'movies':movies
    })
@login_required
def movie_detail(request, slug):
    movie = get_object_or_404(Film, slug=slug)
    screenings = Screening.objects.filter(film=movie)
    return render(request, 'movies/movie_detail.html', {
        'movie':movie,
        "screenings":screenings,
                
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=RegistrationForm()
    return render(request, 'movies/register.html', {
        'form':form
    })

@login_required
def reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'movies/reservation.html', {
        'reservations': reservations
    })
@login_required
def create_reservation(request, screening_id):
    screening_now = get_object_or_404(Screening, id = screening_id)
    Reservation.objects.get_or_create(
        user=request.user,
        screening=screening_now,
        defaults={'tickets_count': 1}
    )
    return redirect('reservation')
    
        
