from django.urls import path, include
from ocorrencia import views as v


app_name = 'ocorrencia'


ocorrencia_patterns = [
    path('', v.OcorrenciaList.as_view(), name="ocorrencias"),
    path('<slug>/detail/', v.ocorrencia, name="ocorrencia"),
    path('add/', v.ocorrencia_create, name="ocorrencia_create"),
    path('add/ajax/', v.ocorrencia_create_ajax, name="ocorrencia_create_ajax"),
    path('<slug>/update/', v.OcorrenciaUpdate.as_view(),
         name="ocorrencia_update"),
]

infracao_patterns = [
    path('', v.InfracaoList.as_view(), name="infracoes"),
    path('add/', v.infracao_create, name="infracao_create"),
    path('<slug>/update/', v.InfracaoUpdate.as_view(), name="infracao_update"),
]

natureza_patterns = [
    path('', v.NaturezaList.as_view(), name="naturezas"),
    path('add/', v.natureza_create, name="natureza_create"),
    path('<slug>/update/', v.NaturezaUpdate.as_view(), name="natureza_update"),
]

homicidio_patterns = [
    path('', v.HomicidioList.as_view(), name="homicidios"),
    path('add/', v.homicidio_create, name="homicidio_create"),
    path('<slug>/update/', v.HomicidioUpdate.as_view(), name="homicidio_update"),
]

urlpatterns = [
    path('ocorrencia/', include(ocorrencia_patterns)),
    path('infracao/', include(infracao_patterns)),
    path('natureza/', include(natureza_patterns)),
    path('homicidio/', include(homicidio_patterns)),
]
