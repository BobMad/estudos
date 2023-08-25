from django.db import models


# Create your models here.
class Disciplina(models.Model):
    disciplina = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    comentarios = models.TextField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()

    def __str__(self):
        return self.disciplina


class Topico(models.Model):
    topico = models.CharField(max_length=250)
    data_criacao = models.DateTimeField()
    comentarios = models.TextField()
    data_atualizacao = models.DateTimeField()

    def __str__(self):
        return self.topico


class Subtopico(models.Model):
    subtopico = models.CharField(max_length=250)
    comentarios = models.TextField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()


class Edital(models.Model):
    orgao = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    data_prova = models.DateTimeField()
    data_edital = models.DateTimeField()
