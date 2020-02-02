from django.urls import path, include
from ocorrencia import views as v


app_name = 'ocorrencia'


ocorrencia_patterns = [
    path('', v.ocorrencias, name="ocorrencias"),
    path('<int:pk>/', v.ocorrencia, name="ocorrencia"),
    path('add/', v.ocorrencia_create, name="ocorrencia_create"),
]

infracao_patterns = [
    path('', v.infracoes, name="infracoes"),
    path('add/', v.infracao_create, name="infracao_create"),
]


urlpatterns = [
    path('ocorrencia/', include(ocorrencia_patterns)),
    path('infracao/', include(infracao_patterns)),
]
