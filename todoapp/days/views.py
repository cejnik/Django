from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def daynumber(request, dayinweek_number):
    return HttpResponse(f'Den: {dayinweek_number}')


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