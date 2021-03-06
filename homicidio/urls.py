from django.urls import include, path

from homicidio import reports as rep
from homicidio import views as v

app_name = 'homicidio'


homicidio_patterns = [
    path('', v.HomicidioList.as_view(), name='homicidio_list'),
    path('add/', v.homicidio_create, name='homicidio_create'),
    path('<slug>/update/', v.HomicidioUpdate.as_view(), name='homicidio_update'),
]

report_patterns = [
    path('', rep.ReportHomicidioList.as_view(), name='report_homicidios'),
]


urlpatterns = [
    path('', include(homicidio_patterns)),
    path('report/', include(report_patterns)),
]
