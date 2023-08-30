from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics
from meusEstudos.models import Disciplina, Topico, Subtopico, Edital
from meusEstudos.serializer import DisciplinaSerializer, EditalSerializer, ListaDisciplinaTopicoSerializer


# Create your views here.
class DisciplinaViewSet(viewsets.ModelViewSet):
    """    Exibindo todas as Disciplinas    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class EditalViewSet(viewsets.ModelViewSet):
    """    Exibindo todos os Editais    """
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer


class ListarDisciplinaViewSet(generics.ListAPIView):
    """ Listando Topicos de Disciplina  """

    def get_queryset(self):
        queryset = Topico.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaDisciplinaTopicoSerializer
