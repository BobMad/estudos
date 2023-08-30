from django.urls import path, include
from rest_framework import routers
from meusEstudos.views import DisciplinaViewSet, EditalViewSet, ListarDisciplinaViewSet

app_name = "meusEstudos"

router = routers.DefaultRouter()
router.register('disciplinas', DisciplinaViewSet, basename='Disciplinas')
router.register('editais', EditalViewSet, basename='Editais')

urlpatterns = [
    path("", include(router.urls)),
    path("disciplina/<int:pk>/topicos/", ListarDisciplinaViewSet.as_view())
]
