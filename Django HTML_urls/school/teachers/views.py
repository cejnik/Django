from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

teachers_info = {
    'snape': 'učitel snape',
    'brumbal': 'učitel brumbal',
    'mcgonagallova': 'učitelka McGonnagallova'
}


def allteachersinfo(request, teachername):
    try:
        info = teachers_info[teachername]
        return HttpResponse(info)
    except:
        return HttpResponseNotFound('Špatná URL adresa')
        

