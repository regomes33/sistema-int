from django.contrib import admin

from .models import Arma, Infracao, Natureza, Operacao


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__', )

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'natureza')
    search_fields = ('natureza',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('operacao', 'descricao')
    search_fields = ('operacao',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'qualificacao', 'arma', 'status')
    search_fields = ('pessoa__nome',)
    list_filter = ('qualificacao', 'arma', 'status')

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
