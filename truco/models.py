from django.db import models

# Create your models here.

class Truco(models.Model):
    nome_music = models.CharField(max_length=255,)
    artista = models.CharField(max_length=50,)
    genero_music = models.CharField(max_length=50,)
    link_music = models.CharField(max_length=255,)