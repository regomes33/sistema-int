from django.urls import path

from .views import listarPessoas
from .views import descricao_pessoa, editar_pessoa,Pdf,person_detail_pdf,validate_editar


urlpatterns = [
    path('', listarPessoas, name='listarpessoas'),
    path('descricao/<int:id>', descricao_pessoa, name='descricao_pessoa'),
    path('editar/<int:id>', editar_pessoa, name='editar_pessoa'),
    path('relatorio_pdf/', Pdf.as_view(), name='relatorio_pdf'),
    path('relatorio_pdf/<int:pk>', person_detail_pdf, name='person_detail_pdf'),
    path('validate_editar/', validate_editar, name="validade_editar"),

]
