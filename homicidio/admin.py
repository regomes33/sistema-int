from django.contrib import admin
from .models import AreaUpm
from .models import Autoria
from .models import Genero
from .models import Homicidio
from .models import Motivacao


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
