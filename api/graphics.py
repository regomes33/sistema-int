from django.db.models import Count
from django.http import JsonResponse

from pessoa.models import Pessoa


def per_status(request):
    status = Pessoa.objects\
        .filter(vitima=False)\
        .values('status_atual')\
        .annotate(value=Count('status_atual'))\
        .order_by('status_atual')\
        .values('status_atual', 'value')
    data = {
        'data': [
            {
                'label': 'livre' if item['status_atual'] == 'solto' else item['status_atual'],
                'value': item['value'],
            }
            for item in status
        ]
    }
    return JsonResponse(data)


def per_faccao(request):
    faccoes = Pessoa.objects\
        .filter(vitima=False)\
        .values('faccao')\
        .annotate(value=Count('faccao'))\
        .order_by('faccao')\
        .values('faccao__nome', 'value')
    data = {
        'data': [
            {
                'label': item['faccao__nome'],
                'value': item['value'],
            }
            for item in faccoes
        ]
    }
    return JsonResponse(data)


def per_city(request):
    cities = Pessoa.objects\
        .filter(vitima=False)\
        .values('district__city')\
        .annotate(value=Count('district__city'))\
        .order_by('district__city')\
        .values('district__city__name', 'value')
    data = {
        'data': [
            {
                'label': item['district__city__name'],
                'value': item['value'],
            }
            for item in cities
        ]
    }
    return JsonResponse(data)
