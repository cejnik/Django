from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JokeForm
from .models import Jokes

# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     visitor_name=request.POST['username']
    #     if visitor_name == '':
    #         return render (request, 'jokesapp/index.html', {
    #             'empty_username': True
    #         })
           
    #     return HttpResponseRedirect('/thank-you')
    #____________________________________________________________________________
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            joke = Jokes(
                user_name = form.cleaned_data['user_name'],
                joke_text = form.cleaned_data['joke_text'],
                rating = form.cleaned_data['rating']
            )
            joke.save()
            return HttpResponseRedirect('/thank-you')
    form = JokeForm()
    return render(request, 'jokesapp/index.html', {
        'jokeForm':form,
    })

def thank_you(request):
    return render(request, 'jokesapp/thank-you.html')

def all_jokes(request):
    database = Jokes.objects.all()
    return render(request, 'jokesapp/all-jokes.html', {
        'database': database
    })