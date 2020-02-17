from django.urls import path
from api import views as v


app_name = 'api'


urlpatterns = [
    path('pessoas/', v.pessoas),
    path('pessoas/add/', v.pessoa_add),
    path('faccoes/', v.faccoes),
    path('naturezas/', v.naturezas),
    path('qualificacoes/', v.qualificacoes),
    path('armas/', v.armas),
    path('status/', v.status),
    path('ocorrencias/', v.ocorrencias),
    path('veiculos/', v.veiculos),
    path('tipo_telefone/', v.tipo_telefone),
    path('ufs/', v.ufs),
]
