from django.contrib import admin
from .models import Comparsa
from .models import Infracao
from .models import Ocorrencia
from .models import Pessoa
from .models import PessoaContato
from .models import PessoaFoto
from .models import PessoaOcorrencia
from .models import Tatuagem


class InfracaoInline(admin.TabularInline):
    model = Infracao
    extra = 0


class PessoaOcorrenciaInline(admin.TabularInline):
    model = PessoaOcorrencia
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (InfracaoInline, PessoaOcorrenciaInline,)
    list_display = ('__str__', 'nome', 'sobrenome', 'mae')
    search_fields = ('nome',)
    list_filter = ('nome',)


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_do_fato')
    search_fields = ('rai', 'descricao')


admin.site.register(Comparsa)
admin.site.register(PessoaContato)
admin.site.register(PessoaFoto)
admin.site.register(Tatuagem)
