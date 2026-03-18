from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

list_of_days = {
    'monday': 'Jít nakoupit',
    'tuesday': 'učit se Python',
    'wednesday': 'Vynést koš',
    'thursday': 'Dojít nakoupit',
    'friday': 'Naprogramovat hru',
    'saturday': 'Zajít do kina',
    'sunday': 'Jít cvičit'
}

def index(request):
    content = ''
    days = list(list_of_days.keys())

    #HTML content
    content = '<ul>'
    for one_day in days:
        url = reverse('days_tasks', args=[one_day]) #reverse vrací URL, redirect vrací HTTP objekt!!
        content += f'<li><a href="{url}">{one_day.capitalize()}</a></li>'
    content += '</ul>'
      #//HTML content
      
    return HttpResponse(content)
  


def daynumber(request, dayinweek_number):
    #vytvoření listu z keys z list_of_days
    days_names =list(list_of_days.keys())
    if dayinweek_number > len(days_names):
        return HttpResponseNotFound('Zadali jste špatné číslo dne.')
    
    redirect_day = days_names[dayinweek_number-1]
    # redirect_path = reverse('days_tasks', args=[redirect_day])
    # return HttpResponseRedirect(redirect_path)
    return redirect('days_tasks', redirect_day)  # vrací na základě importu reverse jako shortscut, vrací HTTPresponse objekt, nikoliv URL

def daytext(request, dayinweek_string):
    try:
        task = list_of_days[dayinweek_string]
        formated_task = f'<h1>{task}</h1>'
        return HttpResponse(formated_task)
    except:
        return HttpResponseNotFound('Špatně zadaný údaj')



