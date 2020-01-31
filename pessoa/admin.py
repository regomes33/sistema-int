from django.contrib import admin
from .models import Pessoa
from .models import PessoaContato
from .models import Comparsa
from .models import PessoaFoto
from .models import Tatuagem
from .models import Ocorrencia
from .models import Infracao


class InfracaoInline(admin.TabularInline):
    model = Infracao
    extra = 0


class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (InfracaoInline, OcorrenciaInline,)
    list_display = ('__str__', 'nome', 'sobrenome', 'mae')
    search_fields = ('nome',)
    list_filter = ('nome',)


admin.site.register(PessoaFoto)
admin.site.register(PessoaContato)
admin.site.register(Comparsa)
admin.site.register(Tatuagem)
