from django.urls import include, path

from api import views as v

app_name = 'api'

pessoas_patterns = [
    path('', v.pessoas),
    path('add/', v.pessoa_add),
    path('add/ajax/', v.pessoa_create_ajax, name='pessoa_create_ajax'),
    path('<int:pessoa_pk>/contato/add/', v.contato_add, name='contato_add'),
    path('<int:pk>/contato/edit/', v.contato_update, name='contato_update'),
    path('veiculos/', v.pessoa_veiculos, name='pessoa_veiculos'),
    path('<int:pessoa_pk>/veiculo/add/', v.veiculo_add, name='veiculo_add'),
    path('<int:pk>/veiculo/edit/', v.veiculo_update, name='veiculo_update'),
    path('<int:pessoa_pk>/comparsa/add/', v.comparsa_add, name='comparsa_add'),
    path('<int:pk>/comparsa/edit/', v.comparsa_update, name='comparsa_update'),
    path('<int:pessoa_pk>/photo/add/', v.photo_add, name='photo_add'),
    path('<int:pk>/photo/edit/', v.photo_update, name='photo_update'),
    path('<int:pessoa_pk>/tattoo/add/', v.tattoo_add, name='tattoo_add'),
    path('<int:pk>/tattoo/edit/', v.tattoo_update, name='tattoo_update'),
    path('ocorrencias/', v.pessoa_ocorrencias, name='pessoa_ocorrencias'),
    path(
        '<int:pessoa_pk>/ocorrencia/add/',
        v.ocorrencia_add,
        name='ocorrencia_add'
    ),
    path(
        '<int:pk>/ocorrencia/edit/',
        v.ocorrencia_update,
        name='ocorrencia_update'
    ),
    path(
        '<int:pessoa_pk>/infracao/add/',
        v.infracao_add,
        name='infracao_add'
    ),
    path(
        '<int:pk>/infracao/edit/',
        v.infracao_update,
        name='infracao_update'
    ),
]

urlpatterns = [
    path('pessoas/', include(pessoas_patterns)),
    path('districts/', v.districts),
    path('districts/<int:pk>/edit/', v.district_update),
    path('comparsas/', v.comparsas, name='comparsas'),
    path('new-comparsa/add/', v.new_comparsa_add, name='new_comparsa_add'),
    path('faccoes/', v.faccoes),
    path('status_atuais/', v.status_atuais),
    path('status_atuais/<int:pk>/edit/', v.status_update),
    path('naturezas/', v.naturezas),
    path('qualificacoes/', v.qualificacoes),
    path('armas/', v.armas),
    path('status/', v.status),
    path('ocorrencias/', v.ocorrencias),
    path('veiculos/', v.veiculos),
    path('tipo_telefone/', v.tipo_telefone),
    path('ufs/', v.ufs),
]
