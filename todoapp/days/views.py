from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

list_of_days = {
    'monday': 'Jít nakoupit',
    'tuesday': 'učit se Python',
    'wednesday': 'Vynést koš',
    'thursday': 'Dojít nakoupit',
    'friday': 'Naprogramovat hru',
    'saturday': 'Zajít do kina',
    'sunday': 'Jít cvičit'
}

def daynumber(request, dayinweek_number):
    #vytvoření listu z keys z list_of_days
    days_names =list(list_of_days.keys())
    if dayinweek_number > len(days_names):
        return HttpResponseNotFound('Zadali jste špatné číslo dne.')
    
    current_day = days_names[dayinweek_number-1]
    return HttpResponseRedirect(current_day)
    

def daytext(request, dayinweek_string):
    day_description = ''
    if dayinweek_string == 'monday':
        day_description = 'Pondělí'
    elif dayinweek_string == 'tuesday':
        day_description = 'úterý'
    elif dayinweek_string == 'wednesday':
        day_description = 'Středa'
    elif dayinweek_string == 'thursday':
        day_description = 'Čtvrtek'
    elif dayinweek_string == 'friday':
        day_description = 'Pátek'
    elif dayinweek_string == 'saturday':
        day_description = 'sobota'
    elif dayinweek_string == 'sunday':
        day_description = 'neděle'
    else:
        return HttpResponseNotFound("Neexistují den")


    return HttpResponse(f'Jaký je den: {day_description}')