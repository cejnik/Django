from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def martinstudent(request):
#     return HttpResponse('Informace o Martinovi')

students_info = {
    'hermiona': 'hermiona je žena',
    'martin': 'martin je....',
    'ron': 'ron je....'
}

# Create your views here.
def allstudentsinfo(request, studentsname):
    try:
        result_info = students_info[studentsname]
        return HttpResponse (result_info)
    except:
        return HttpResponseNotFound('Zadané špatné jméno')
