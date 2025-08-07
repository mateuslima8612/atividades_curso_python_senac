from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def criticas(request):
    return render(request, 'criticas.html')

def embreve(request):
    return render(request, 'embreve.html')

def filmes(request):
    return render(request, 'filmes.html')

def noticias(request):
    return render(request, 'noticias.html')

def series(request):
    return render(request, 'series.html')