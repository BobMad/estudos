from django.db import models


# Create your models here.
class Disciplinas(models.Model):
    disciplina = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    comentarios = models.TextField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()


class Topicos(models.Model):
    topico = models.CharField(max_length=250)
    data_criacao = models.DateTimeField()
    comentarios = models.TextField()
    data_atualizacao = models.DateTimeField()


class Subtopicos(models.Model):
    subtopico = models.CharField(max_length=250)
    comentarios = models.TextField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()


class Editais(models.Model):
    orgao = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    data_prova = models.DateTimeField()
    data_inicio = models.DateTimeField()
