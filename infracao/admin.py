from django.contrib import admin
from .models import Arma
from .models import Natureza
from .models import Infracao


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


@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'qualificacao', 'arma', 'status')
    search_fields = ('pessoa__nome',)
    list_filter = ('qualificacao', 'arma', 'status')

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
