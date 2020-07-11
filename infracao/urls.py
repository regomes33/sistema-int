from django.urls import path, include
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


urlpatterns = [
    path('infracao/', include(infracao_patterns)),
    path('natureza/', include(natureza_patterns)),
]
