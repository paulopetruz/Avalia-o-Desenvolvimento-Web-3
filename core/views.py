from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def feriados(request):
    contexto = {'Feriado': True,
                '':False}
    return render(request, 'Feriado.html', contexto)