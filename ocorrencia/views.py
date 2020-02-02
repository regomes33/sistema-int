from django.shortcuts import render
from .models import Ocorrencia


def ocorrencias(request):
    template_name = 'ocorrencias.html'
    object_list = Ocorrencia.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def ocorrencia(request, pk):
    template_name = 'ocorrencia.html'
    obj = Ocorrencia.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
