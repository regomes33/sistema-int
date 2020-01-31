from django.urls import path, include
from .views import inicial, registrarusuario


urlpatterns = [
    path('', inicial, name="inicial"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrar/', registrarusuario, name='registrar'),
]
