from rest_framework import serializers
from meusEstudos.models import Disciplina, Topico, Subtopico, Edital

class DiscipliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['disciplina', 'sigla', 'comentarios']
        # fields = '__all__'

