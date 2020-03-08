from django.conf import settings
from django.contrib import admin
from ocorrencia.models import Infracao
from ocorrencia.models import PessoaOcorrencia
from .models import Comparsa
from .models import Faccao
from .models import Foto
from .models import Pessoa
from .models import PessoaContato
from .models import PessoaVeiculo
from .models import Tatuagem


class FotoInline(admin.TabularInline):
    model = Foto
    extra = 0


class TatuagemInline(admin.TabularInline):
    model = Tatuagem
    extra = 0


class InfracaoInline(admin.TabularInline):
    model = Infracao
    extra = 0


class PessoaOcorrenciaInline(admin.TabularInline):
    model = PessoaOcorrencia
    extra = 0


class PessoaContatoInline(admin.TabularInline):
    model = PessoaContato
    extra = 0


class ComparsaInline(admin.TabularInline):
    model = Comparsa
    # fields = ('nome', 'rg', 'cpf', 'cnh')
    extra = 0


class PessoaVeiculoInline(admin.TabularInline):
    model = PessoaVeiculo
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (
        FotoInline,
        TatuagemInline,
        InfracaoInline,
        PessoaOcorrenciaInline,
        PessoaContatoInline,
        ComparsaInline,
        PessoaVeiculoInline
    )
    list_display = ('__str__', 'slug', 'nome',
                    'sobrenome', 'apelido', 'faccao')
    search_fields = ('nome', 'sobrenome', 'apelido', 'mae', 'pai')
    list_filter = ('faccao',)
    date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PessoaContato)
class PessoaContatoAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'slug', 'pessoa')
    search_fields = ('pessoa__nome', 'telefone')

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Comparsa)
class ComparsaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug',)
    # search_fields = ('nome',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tatuagem)
class TatuagemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug',)
    search_fields = (
        'pessoa__nome',
        'pessoa__sobrenome',
        'pessoa__apelido',
        'descricao'
    )

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Faccao)
class FaccaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'funcao')
    search_fields = ('nome',)
    list_filter = ('funcao',)

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PessoaVeiculo)
class PessoaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    # search_fields = ('',)
    date_hierarchy = 'created'

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')

    # if not settings.DEBUG:
    def has_delete_permission(self, request, obj=None):
        return False
