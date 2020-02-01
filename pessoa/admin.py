from django.contrib import admin
from .models import Comparsa
from .models import Faccao
from ocorrencia.models import Infracao
from .models import Pessoa
from .models import PessoaContato
from .models import PessoaFoto
from ocorrencia.models import PessoaOcorrencia
from .models import PessoaVeiculo
from .models import Tatuagem


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
    fields = ('nome', 'rg', 'cpf', 'cnh')
    extra = 0


class PessoaVeiculoInline(admin.TabularInline):
    model = PessoaVeiculo
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (
        InfracaoInline,
        PessoaOcorrenciaInline,
        PessoaContatoInline,
        ComparsaInline,
        PessoaVeiculoInline
    )
    list_display = ('__str__', 'nome', 'sobrenome', 'apelido', 'faccao')
    search_fields = ('nome', 'sobrenome', 'apelido', 'mae', 'pai')
    list_filter = ('faccao',)
    date_hierarchy = 'created'


@admin.register(PessoaContato)
class PessoaContatoAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'pessoa')
    search_fields = ('pessoa__nome', 'telefone')


@admin.register(Comparsa)
class ComparsaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('nome_comparsa',)


@admin.register(Tatuagem)
class TatuagemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = (
        'pessoa__nome',
        'pessoa__sobrenome',
        'pessoa__apelido',
        'descricao'
    )


@admin.register(Faccao)
class FaccaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'funcao')
    search_fields = ('nome',)
    list_filter = ('funcao',)


@admin.register(PessoaVeiculo)
class PessoaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    # search_fields = ('',)
    date_hierarchy = 'created'


admin.site.register(PessoaFoto)
