from django.contrib import admin
from .models import Pessoa
from .models import PessoaContato
from .models import PessoaEndereco
from .models import Comparsas
from .models import PessoaFoto
from .models import Tatuagem
from infracao.models import Ocorrencias, Infracao


admin.site.register(PessoaFoto)
admin.site.register(PessoaContato)
admin.site.register(PessoaEndereco)
admin.site.register(Comparsas)
admin.site.register(Tatuagem)


class InfracaoInline(admin.TabularInline):
    model = Infracao
    extra = 0


class OcorrenciasInline(admin.TabularInline):
    model = Ocorrencias
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (InfracaoInline, OcorrenciasInline,)
    list_display = ('__str__', 'nome', 'sobrenome', 'mae')
    search_fields = ('nome',)
    list_filter = ('nome',)
