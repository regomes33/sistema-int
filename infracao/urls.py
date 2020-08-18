from django.urls import include, path

from infracao import views as v

app_name = 'infracao'


infracao_patterns = [
    path('', v.InfracaoList.as_view(), name='infracao_list'),
    path('add/', v.infracao_create, name='infracao_create'),
    path('<slug>/update/', v.InfracaoUpdate.as_view(), name='infracao_update'),
]

natureza_patterns = [
    path('', v.NaturezaList.as_view(), name='natureza_list'),
    path('add/', v.natureza_create, name='natureza_create'),
    path('<slug>/update/', v.NaturezaUpdate.as_view(), name='natureza_update'),
]

operacao_patterns = [
    path('', v.OperacaoList.as_view(), name='operacao_list'),
    path('add/', v.operacao_create, name='operacao_create'),
    path('<slug>/update/', v.OperacaoUpdate.as_view(), name='operacao_update'),
]

urlpatterns = [
    path('infracao/', include(infracao_patterns)),
    path('natureza/', include(natureza_patterns)),
    path('operacao/', include(operacao_patterns)),
]
