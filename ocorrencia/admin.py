from django.contrib import admin

from .models import Ocorrencia, OcorrenciaVeiculo


class OcorrenciaVeiculoInline(admin.TabularInline):
    model = OcorrenciaVeiculo
    extra = 0


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    inlines = (OcorrenciaVeiculoInline,)
    list_display = ('__str__', 'slug', 'data_do_fato')
    search_fields = ('rai', 'descricao')
    date_hierarchy = 'created'
    ordering = ('rai',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False
