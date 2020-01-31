from django.urls import path, include

from .views import pessoaCadastro, validate_cpf

urlpatterns = [
    path('', pessoaCadastro, name="pessoa"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('validate_cpf/', validate_cpf, name="validade_cpf"),

]


urlpatterns = [
    path('', infracaoCadastro, name="infracao"),
    path('accounts/', include('django.contrib.auth.urls')),

]


urlpatterns = [
    path('', listarPessoas, name='listarpessoas'),
    path('descricao/<int:id>/', descricao_pessoa, name='descricao_pessoa'),
    path('editar/<int:id>/', editar_pessoa, name='editar_pessoa'),
    path('relatorio_pdf/', Pdf.as_view(), name='relatorio_pdf'),
    path('relatorio_pdf/<int:pk>/', person_detail_pdf, name='person_detail_pdf'),
    path('validate_editar/', validate_editar, name="validade_editar"),

]
