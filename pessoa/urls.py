from django.urls import path, include
from pessoa import views as v
from pessoa import reports as rep


app_name = 'pessoa'


pessoa_patterns = [
    path('', v.PessoasList.as_view(), name='pessoa_list'),
    path('<slug>/detail/', v.pessoa_detail, name='pessoa_detail'),
    path('add/', v.pessoa_create, name='pessoa_create'),
    path('<slug>/edit/', v.pessoa_update, name='pessoa_update'),
]

report_patterns = [
    path('', rep.report_pessoas, name='report_pessoa_list'),
    path('<slug>/detail/', rep.report_pessoa, name='report_pessoa_detail'),
]

urlpatterns = [
    path('', include(pessoa_patterns)),
    path('report/', include(report_patterns)),
]
