from django.urls import path, include
from core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name="inicial"),
    path('registrar/', v.registrarusuario, name='registrar'),
    path('accounts/', include('django.contrib.auth.urls')),
]
