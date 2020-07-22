from django.conf import settings
from django.contrib import admin

from .models import Cor, Modelo, Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('slug', 'placa', 'modelo', 'cor')
    search_fields = ('placa', 'modelo__modelo', 'cor')
    list_filter = ('modelo', 'cor')

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    search_fields = ('modelo',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    search_fields = ('cor',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
