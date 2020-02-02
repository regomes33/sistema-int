from django.urls import path, include
from pessoa import views as v


app_name = 'pessoa'


pessoa_patterns = [
    path('', v.pessoas, name="pessoas"),
    path('<int:pk>/', v.pessoa, name="pessoa"),
    # path('add/', v.pessoa_create, name="pessoa_create"),
]


urlpatterns = [
    path('', include(pessoa_patterns)),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', pessoaCadastro, name="pessoa"),
    # path('validate_cpf/', validate_cpf, name="validade_cpf"),
    # path('', infracaoCadastro, name="infracao"),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('descricao/<int:id>/', descricao_pessoa, name='descricao_pessoa'),
    # path('editar/<int:id>/', editar_pessoa, name='editar_pessoa'),
    # path('relatorio_pdf/', Pdf.as_view(), name='relatorio_pdf'),
    # path('relatorio_pdf/<int:pk>/', person_detail_pdf, name='person_detail_pdf'),
    # path('validate_editar/', validate_editar, name="validade_editar"),
]
