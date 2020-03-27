from django.urls import include, path
from api import views as v


app_name = 'api'

pessoas_patterns = [
    path('', v.pessoas),
    path('add/', v.pessoa_add),
    path('add/ajax/', v.pessoa_create_ajax, name="pessoa_create_ajax"),
    path('<int:pk>/contato/edit/', v.contato_update, name="contato_update"),
    path('veiculos/', v.pessoa_veiculos, name="pessoa_veiculos"),
    path('<int:pk>/veiculo/edit/', v.veiculo_update, name="veiculo_update"),
    path('<int:pk>/comparsa/edit/', v.comparsa_update, name="comparsa_update"),
]

urlpatterns = [
    path('pessoas/', include(pessoas_patterns)),
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
