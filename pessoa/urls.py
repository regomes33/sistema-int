from django.urls import path, include
from pessoa import views as v


app_name = 'pessoa'


pessoa_patterns = [
    path('', v.PessoasList.as_view(), name="pessoas"),
    path('<slug>/detail/', v.pessoa, name="pessoa"),
    path('add/', v.pessoa_create, name="pessoa_create"),
    path('<slug>/edit/', v.pessoa_update, name="pessoa_update"),
    path('<int:pk>/contato/edit/', v.contato_update, name="contato_update"),
]

urlpatterns = [
    path('', include(pessoa_patterns)),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('relatorio_pdf/', Pdf.as_view(), name='relatorio_pdf'),
    # path('relatorio_pdf/<int:pk>/', person_detail_pdf, name='person_detail_pdf'),
    # path('validate_editar/', validate_editar, name="validade_editar"),
]
