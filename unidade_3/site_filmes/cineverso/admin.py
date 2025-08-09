from django.contrib import admin
from .models import Filme, Genero, Ator, Critica

admin.site.register(Filme)
admin.site.register(Genero)
admin.site.register(Ator)
admin.site.register(Critica)
