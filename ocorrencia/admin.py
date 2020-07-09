from django.conf import settings
from django.contrib import admin
from .models import Arma
from .models import Infracao
from .models import Natureza
from .models import Ocorrencia
from .models import OcorrenciaVeiculo
from .models import AreaUpm
from .models import Motivacao
from .models import Homicidio
from .models import Genero
from .models import Autoria


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    search_fields = ('arma',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('artigo', '__str__', 'slug')
    list_display_links = ('__str__',)
    search_fields = ('natureza',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


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


@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'qualificacao', 'arma', 'status',)
    list_filter = ('qualificacao', 'arma', 'status',)
    date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AreaUpm)
class AreaUpmAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug',)
    list_filter = ('area_upm',)
    # date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Motivacao)
class MotivacaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    # list_filter = ('qualificacao', 'arma', 'status',)
    # date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Autoria)
class AutoriaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    # list_filter = ('qualificacao', 'arma', 'status',)
    # date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    # list_filter = ('qualificacao', 'arma', 'status',)
    # date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Homicidio)
class HomicidioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'data_do_homicidio',
                    'forma', 'area_upm', 'vitima', 'motivacao')
    search_fields = ('vitima__nome',)
    readonly_fields = ('slug',)
    list_filter = ('forma', 'district', 'area_upm',
                   'motivacao', 'data_do_homicidio')
    date_hierarchy = 'created'

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False
