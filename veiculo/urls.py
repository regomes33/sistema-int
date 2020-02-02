from django.urls import path, include
from veiculo import views as v


app_name = 'veiculo'


veiculo_patterns = [
    path('', v.veiculos, name="veiculos"),
    path('add/', v.veiculo_create, name="veiculo_create"),
]


urlpatterns = [
    path('veiculo/', include(veiculo_patterns)),
]
