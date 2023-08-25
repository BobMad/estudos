from django.contrib import admin

from meusEstudos.models import Disciplina, Topico, Subtopico, Edital


# Register your models here.
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'sigla', 'data_atualizacao', 'data_criacao']


admin.site.register(Disciplina, DisciplinaAdmin)


class TopicoAdmin(admin.ModelAdmin):
    list_display = ['topico', 'data_atualizacao']


class SubtopicoAdmin(admin.ModelAdmin):
    list_display = ['subtopico', 'data_atualizacao']


class EditalAdmin(admin.ModelAdmin):
    list_display = ['orgao', 'cargo', 'data_edital', 'data_prova']


admin.site.register(Topico, TopicoAdmin)
admin.site.register(Subtopico, SubtopicoAdmin)
admin.site.register(Edital, EditalAdmin)
