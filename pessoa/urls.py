from django.urls import path, include
from pessoa import views as v
from pessoa import reports as rep


app_name = 'pessoa'


pessoa_patterns = [
    path('', v.PessoasList.as_view(), name='pessoas'),
    path('<slug>/detail/', v.pessoa, name='pessoa'),
    path('add/', v.pessoa_create, name='pessoa_create'),
    path('<slug>/edit/', v.pessoa_update, name='pessoa_update'),
]

report_patterns = [
    path('', rep.report_pessoas, name='report_pessoas'),
    path('<slug>/detail/', rep.report_pessoa, name='report_pessoa'),
]

urlpatterns = [
    path('', include(pessoa_patterns)),
    path('report/', include(report_patterns)),
    # path('accounts/', include('django.contrib.auth.urls')),
]
