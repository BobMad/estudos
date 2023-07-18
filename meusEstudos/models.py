from django.db import models


# Create your models here.
class Disciplinas(models.Model):
    disciplina = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()


class Topicos(models.Model):
    topico = models.CharField(max_length=250)
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()


class Subtopico(models.Model):
    subtopico = models.CharField(max_length=250)
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()
