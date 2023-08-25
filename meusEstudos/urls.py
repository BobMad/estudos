from django.urls import path, include
from rest_framework import routers
from meusEstudos.views import DisciplinaViewSet

app_name = "meusEstudos"

router = routers.DefaultRouter()
router.register('disciplinas', DisciplinaViewSet, basename='Disciplinas')

urlpatterns = [
    path("", include(router.urls)),
]
