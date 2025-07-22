from django.contrib import admin
from .models import Fator, Acao, Pergunta, LogAcao

@admin.register(Fator)
class FatorAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'nome', 'classificacao_risco')  # colunas que aparecerão na lista
    ordering = ('ordem',)

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('fator', 'classificacao', 'descricao')
    ordering = ('fator',)

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'fator')
    ordering = ('fator',)

@admin.register(LogAcao)
class LogAcaoAdmin(admin.ModelAdmin):
    list_display = ('executado_por', 'acao', 'usuario_alvo', 'data_hora')
    ordering = ('-data_hora',)
