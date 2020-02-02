from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import OcorrenciaForm
from .models import Ocorrencia, Infracao


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


def ocorrencia_create(request):
    form = OcorrenciaForm(request.POST or None)
    template_name = 'ocorrencia_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ocorrencia:ocorrencias'))

    context = {'form': form}
    return render(request, template_name, context)


def infracoes(request):
    template_name = 'infracoes.html'
    object_list = Infracao.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)