from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def index(request):
    content = ''
    greeting_list = list(greet_list.keys())
    content +='<ul>'
    for one_greet in greeting_list:
        url = reverse('greeting_string', args=[one_greet])
        content += f'<li><a href="{url}">{one_greet}</li>'
    content += '</ul>'
    return HttpResponse(content)

greet_list = {
    'ahoj':'nic',
    'cau':'tak zase nic',
    'dobrý den':'nic....'
    }

def greet_string(request, greet_string):
    greet_name = greet_list[greet_string]
    return HttpResponse(greet_name)

def greet_number(request, greet_number):
    greeting_list = list(greet_list.keys())
    if greet_number > len(greeting_list):
        return HttpResponseNotFound("Pozdrav nenalezen")
    current_greet = greeting_list[greet_number-1]
    return redirect('greeting_string', current_greet)