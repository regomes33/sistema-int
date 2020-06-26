from django.db.models import Q
from datetime import datetime
from django.shortcuts import render
from .models import Homicidio


def report_homicidios(request):
    homicidios = Homicidio.objects.all()

    filter_forma = request.GET.get('filter_forma')
    filter_area_upm = request.GET.get('filter_area_upm')
    filter_motivacao = request.GET.get('filter_motivacao')
    filter_bairro = request.GET.get('filter_bairro')

    if filter_forma:
        homicidios = homicidios.filter(Q(forma=filter_forma))

    if filter_area_upm:
        homicidios = homicidios.filter(Q(area_upm=filter_area_upm))

    if filter_motivacao:
        homicidios = homicidios.filter(Q(motivacao=filter_motivacao))

    if filter_bairro:
        homicidios = homicidios.filter(Q(district=filter_bairro))

    context = {
        'object_list': homicidios,
        'today': datetime.now().today()
    }
    template_name = 'relatorios/report_homicidios.html'
    return render(request, template_name, context)


# def report_homicidios(request):
#     homicidios = Homicidio.objects.all()

#     context = {
#         'object_list': homicidios,
#         'today': datetime.now().today()
#     }
#     template_name = 'relatorios/report_homicidios.html'
#     return render(request, template_name, context)
