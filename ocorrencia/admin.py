from django.contrib import admin
from .models import Arma
from .models import Infracao
from .models import Natureza
from .models import Ocorrencia


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('arma',)


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('natureza',)


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_do_fato')
    search_fields = ('rai', 'descricao')


@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
