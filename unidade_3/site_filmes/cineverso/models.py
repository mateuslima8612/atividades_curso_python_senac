from django.db import models
from django.contrib.auth.models import User

#FILMES E SERIES

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='imagens-mateus/')
    genero = models.ManyToManyField(Genero, related_name='filmes')
    elenco = models.ManyToManyField(Ator, related_name='filmes')
    dt_lançamento = models.DateField()

    def __str__(self):
        return self.titulo

class Serie(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.URLField(max_length=200)
    genero = models.ManyToManyField(Genero, related_name='series')
    elenco = models.ManyToManyField(Ator, related_name='series')
    dt_lançamento = models.DateField()

    def __str__(self):
        return self.titulo
    
#CRITICAS

class Critica(models.Model):
    texto = models.TextField()
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
















# from django.db import models

# class Ator(models.Model):
#     id_ator = models.CharField(max_length=50, primary_key=True)
#     nome = models.CharField(max_length=100)
#     dt_nascimento = models.DateField()
#     filmes = models.TextField()

# class Filme(models.Model):
#     id_filme = models.CharField(max_length=50, primary_key=True)
#     titulo = models.CharField(max_length=100)
#     descricao = models.TextField()
#     cover = models.URLField(max_length=200)
#     genero = models.CharField(max_length=20)
#     elenco = models.TextField()

# class Genero(models.Model):
#     id_genero = models.CharField(max_length=50, primary_key=True)
#     genero_nome = models.TextField()
#     id_filme = models.ForeignKey()


