from django.shortcuts import render
from .models import Filme

# Create your views here.

def home(request):
    return render(request, 'home.html')

def criticas(request):
    return render(request, 'criticas.html')

def embreve(request):
    return render(request, 'embreve.html')

def filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes.html', {'lista_filmes': filmes})

def noticias(request):
    return render(request, 'noticias.html')

def series(request):
    return render(request, 'series.html')