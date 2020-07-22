from django.urls import include, path

from veiculo import views as v

app_name = 'veiculo'


veiculo_patterns = [
    path('', v.VeiculoList.as_view(), name='veiculo_list'),
    path('add/', v.veiculo_create, name='veiculo_create'),
    path('<slug>/update/', v.VeiculoUpdate.as_view(), name='veiculo_update'),
]

modelo_patterns = [
    path('', v.ModeloList.as_view(), name='modelo_list'),
    path('add/', v.modelo_create, name='modelo_create'),
    path('<slug>/update/', v.ModeloUpdate.as_view(), name='modelo_update'),
]


urlpatterns = [
    path('veiculo/', include(veiculo_patterns)),
    path('modelo/', include(modelo_patterns)),
]
