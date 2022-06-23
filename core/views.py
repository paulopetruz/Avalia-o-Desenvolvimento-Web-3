from http.client import HTTPResponse
from django.shortcuts import render

def feriado(request):
    return render(request, 'index.html')
# Create your views here.
