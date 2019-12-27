from django.urls import path, include

from .views import inicial


urlpatterns = [

    path('', inicial, name="inicial"),
    path('accounts/', include('django.contrib.auth.urls'))
]