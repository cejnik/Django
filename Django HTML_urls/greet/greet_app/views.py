from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound 
from django.urls import reverse

greet_list = {
    'ahoj': 'nic',
    'cau': 'tak zase nic',
    'dobrý den': 'nic....',
}


def index(request):
    content = '<ul>'
    for one_greet in greet_list.keys():
        url = reverse('greeting_string', args=[one_greet])
        content += f'<li><a href="{url}">{one_greet}</a></li>'
    content += '</ul>'
    return HttpResponse(content)


def greet_string(request, greet_string):
    greet_name = greet_list.get(greet_string)
    if greet_name is None:
        return HttpResponseNotFound("Pozdrav nenalezen")
    return HttpResponse(greet_name)


def greet_number(request, greet_number):
    greeting_list = list(greet_list.keys())
    if greet_number > len(greeting_list) or greet_number < 1:
        return HttpResponseNotFound("Pozdrav nenalezen")
    current_greet = greeting_list[greet_number - 1]
    return redirect('greeting_string', current_greet)