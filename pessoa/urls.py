from django.urls import include, path

from pessoa import reports as rep
from pessoa import views as v

app_name = 'pessoa'


pessoa_patterns = [
    path('', v.PessoasList.as_view(), name='pessoa_list'),
    path('<slug>/detail/', v.pessoa_detail, name='pessoa_detail'),
    path('add/', v.pessoa_create, name='pessoa_create'),
    path('<slug>/edit/', v.pessoa_update, name='pessoa_update'),
]

comparsa_patterns = [
    path('', v.ComparsaList.as_view(), name='comparsa_list'),
    path('add/', v.ComparsaCreate.as_view(), name='comparsa_create'),
    path('<slug>/edit/', v.ComparsaUpdate.as_view(), name='comparsa_update'),
]

report_patterns = [
    path('', rep.ReportPessoasList.as_view(), name='report_pessoa_list'),
    path('<slug>/detail/', rep.report_pessoa, name='report_pessoa_detail'),
]

urlpatterns = [
    path('', include(pessoa_patterns)),
    path('comparsa/', include(comparsa_patterns)),
    path('report/', include(report_patterns)),
]
