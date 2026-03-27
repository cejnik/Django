from django.shortcuts import render
import json
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def api(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'data.json')   
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return Response(data)