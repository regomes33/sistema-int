from django.contrib import admin
from .models import Arma
from .models import Infracao
from .models import Natureza
from .models import Ocorrencia
from .models import OcorrenciaVeiculo


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('arma',)


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('natureza',)


class OcorrenciaVeiculoInline(admin.TabularInline):
    model = OcorrenciaVeiculo
    extra = 0


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    inlines = (OcorrenciaVeiculoInline,)
    list_display = ('__str__', 'data_do_fato')
    search_fields = ('rai', 'descricao')
    date_hierarchy = 'created'


@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'qualificacao', 'arma', 'status',)
    list_filter = ('qualificacao', 'arma', 'status',)
    date_hierarchy = 'created'
