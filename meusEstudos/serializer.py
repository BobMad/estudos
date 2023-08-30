from rest_framework import serializers, generics
from meusEstudos.models import Disciplina, Topico, Subtopico, Edital


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['disciplina', 'sigla', 'comentarios']
        # fields = '__all__'


class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        exclude = []


class ListaDisciplinaTopicoSerializer(serializers.ModelSerializer):
    """ Listando Topicos de Disciplina  """
    class Meta:
        model = Edital
        fields = ['disciplina', 'topico']