from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from meusEstudos.models import Disciplina, Topico, Subtopico, Edital
from meusEstudos.serializer import DiscipliaSerializer


# Create your views here.
class DisciplinaViewSet(viewsets.ModelViewSet):
    """    Exibindo todas as Disciplinas    """
    queryset = Disciplina.objects.all()
    serializer_class = DiscipliaSerializer
