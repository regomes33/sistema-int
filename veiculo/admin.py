from django.contrib import admin
from .models import Cor
from .models import Modelo
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'cor')
    search_fields = ('placa', 'modelo__modelo', 'cor')
    list_filter = ('modelo', 'cor')


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('modelo',)


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('cor',)
