from django.shortcuts import render
from school.models import Student

# Create your views here.

def index (request):
    students = Student.objects.all()
    return render(request, 'school/index.html', {
        'students':students
    })

def premiants(request):
    all_premiants = Student.objects.filter(is_premiant=True)
    return render(request, 'school/premiants.html', {
        'premiants': all_premiants
    })