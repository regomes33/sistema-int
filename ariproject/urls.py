from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path(
        'accounts/logout/',
        LogoutView.as_view(),
        # {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'
    ),
    path('api/', include('api.urls', namespace='api')),
    path('homicidio/', include('homicidio.urls', namespace='homicidio')),
    path('infracao/', include('infracao.urls', namespace='infracao')),
    path('ocorrencia/', include('ocorrencia.urls', namespace='ocorrencia')),
    path('pessoa/', include('pessoa.urls', namespace='pessoa')),
    path('veiculo/', include('veiculo.urls', namespace='veiculo')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
