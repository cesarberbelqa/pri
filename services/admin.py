from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'preco', 'duracao', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('titulo', 'descricao')
    list_editable = ('preco', 'ativo')
    readonly_fields = ('data_criacao', 'data_atualizacao', 'data_delecao')