from django.contrib import admin
from .models import Ocorrencia
from .models import OcorrenciaVeiculo


class OcorrenciaVeiculoInline(admin.TabularInline):
    model = OcorrenciaVeiculo
    extra = 0


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    inlines = (OcorrenciaVeiculoInline,)
    list_display = ('__str__', 'slug', 'data_do_fato')
    search_fields = ('rai', 'descricao')
    date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
