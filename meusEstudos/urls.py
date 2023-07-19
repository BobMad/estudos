from django.urls import path

from . import views

app_name = "meusEstudos"
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:disciplina_id>', views.index, name='disciplinas'),
]