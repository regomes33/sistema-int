from django.db.models import Q
from datetime import datetime
from django.shortcuts import render
from .models import Homicidio


def report_homicidios(request):
    homicidios = Homicidio.objects.all()

    context = {
        'object_list': homicidios,
        'today': datetime.now().today()
    }
    template_name = 'relatorios/report_homicidios.html'
    return render(request, template_name, context)
