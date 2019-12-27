from django.urls import path, include
from .views import infracaoCadastro

urlpatterns = [
    path('', infracaoCadastro, name="infracao"),
    path('accounts/', include('django.contrib.auth.urls')),
]