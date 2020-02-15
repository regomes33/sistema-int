from django.urls import path
from api import views as v


app_name = 'api'


urlpatterns = [
    path('pessoas/', v.pessoas),
    path('pessoas/add/', v.pessoa_add),
    path('naturezas/', v.naturezas),
    path('qualificacoes/', v.qualificacoes),
    path('armas/', v.armas),
    path('status/', v.status),
    path('veiculos/', v.veiculos),
]
