from django.urls import path
from ocorrencia import views as v


app_name = 'ocorrencia'


urlpatterns = [
    path('', v.ocorrencias, name="ocorrencias"),
    path('<int:pk>/', v.ocorrencia, name="ocorrencia"),
]
