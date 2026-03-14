from django.shortcuts import render

def starting_page(request):
    return render(request, 'netflix/index.html') # divá se automaticky pod templates

