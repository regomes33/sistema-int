from django.urls import path, include

from .views import pessoaCadastro, validate_cpf

urlpatterns = [
    path('', pessoaCadastro, name="pessoa"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('validate_cpf/',validate_cpf, name="validade_cpf"),

]

