from django.urls import include, path

from ocorrencia import views as v

app_name = 'ocorrencia'


ocorrencia_patterns = [
    path('', v.OcorrenciaList.as_view(), name='ocorrencia_list'),
    path('add/', v.ocorrencia_create, name='ocorrencia_create'),
    path('add/ajax/', v.ocorrencia_create_ajax, name='ocorrencia_create_ajax'),
    path('<slug>/update/', v.OcorrenciaUpdate.as_view(), name='ocorrencia_update'),
]


urlpatterns = [
    path('ocorrencia/', include(ocorrencia_patterns)),
]
