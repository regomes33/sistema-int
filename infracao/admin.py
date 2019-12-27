from django.contrib import admin

from .models import Infracao,Modusoperandi,Ocorrencias
# Register your models here.

admin.site.register(Infracao)
admin.site.register(Modusoperandi)
admin.site.register(Ocorrencias)