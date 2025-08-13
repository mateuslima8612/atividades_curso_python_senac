from django.shortcuts import render
from .models import Filme, Serie

# Create your views here.

def home(request):
    filmes = Filme.objects.all()
    ultimos_filmes = filmes.order_by('-id')[:5]

    series = Serie.objects.all()
    ultimas_series = series.order_by('-id')[:5]
    return render(request, 'home.html', {'lista_filmes': filmes, 'ultimos_filmes': ultimos_filmes, 'lista_series': series, 'ultimas_series': ultimas_series})

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
    series = Serie.objects.all()
    return render(request, 'series.html', {'lista_series': series})