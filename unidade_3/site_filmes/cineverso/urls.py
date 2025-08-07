from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criticas', views.criticas, name='criticas'),
    path('embreve', views.embreve, name='embreve'),
    path('filmes', views.filmes, name='filmes'),
    path('noticias', views.noticias, name='noticias'),
    path('series', views.series, name='series')
]