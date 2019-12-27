from django.contrib import admin
from .models import Pessoa
from .models import PessoaContato

from .models import PessoaEndereco
from .models import Comparsas
from .models import PessoaFoto
from .models import Tatuagem
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(PessoaFoto)
admin.site.register(PessoaContato)

admin.site.register(PessoaEndereco)
admin.site.register(Comparsas)
admin.site.register(Tatuagem)

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('_str_','nome','sobrenome','mae')
    search_fields = ('nome')
    list_filter = ('nome')

