from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import OcorrenciaForm, InfracaoForm, NaturezaForm, HomicidioForm
from .models import Ocorrencia, Infracao, Natureza, Homicidio


def ocorrencias(request):
    template_name = 'ocorrencias.html'
    object_list = Ocorrencia.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(rai__icontains=search) |
            Q(descricao__icontains=search)
        )

    context = {
        'object_list': object_list,
        'model_name_plural': 'Ocorrências',
    }
    return render(request, template_name, context)


def ocorrencia(request, pk):
    template_name = 'ocorrencia.html'
    obj = Ocorrencia.objects.get(pk=pk)
    context = {
        'object': obj,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencias'),
    }
    return render(request, template_name, context)


def ocorrencia_create(request):
    form = OcorrenciaForm(request.POST or None)
    template_name = 'ocorrencia_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:ocorrencias'))

    context = {
        'form': form,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencias'),
    }
    return render(request, template_name, context)


def infracoes(request):
    template_name = 'infracoes.html'
    object_list = Infracao.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(natureza__natureza__icontains=search)
        )

    context = {
        'object_list': object_list,
        'model_name_plural': 'Infrações',
    }
    return render(request, template_name, context)


def infracao_create(request):
    form = InfracaoForm(request.POST or None)
    template_name = 'infracao_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:infracoes'))

    context = {
        'form': form,
        'model_name_plural': 'Infrações',
        'url': reverse('ocorrencia:infracoes'),
    }
    return render(request, template_name, context)


def naturezas(request):
    template_name = 'naturezas.html'
    object_list = Natureza.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(natureza__icontains=search)

    context = {
        'object_list': object_list,
        'model_name_plural': 'Naturezas',
    }
    return render(request, template_name, context)


def natureza_create(request):
    form = NaturezaForm(request.POST or None)
    template_name = 'natureza_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ocorrencia:naturezas'))

    context = {
        'form': form,
        'model_name_plural': 'Naturezas',
        'url': reverse('ocorrencia:naturezas'),
    }
    return render(request, template_name, context)


def homicidios(request):
    template_name = 'homicidios.html'
    object_list = Homicidio.objects.all()

    # search = request.GET.get('search')
    # if search:
    #     object_list = object_list.filter(
    #         Q(forma__icontains=search)
    #     )

    context = {
        'object_list': object_list,
        'model_name_plural': 'Homicidios',
    }
    return render(request, template_name, context)


def homicidio_create(request):
    form = HomicidioForm(request.POST or None)
    template_name = 'homicidio_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:homicidios'))

    context = {
        'form': form,
        'model_name_plural': 'Homicidios',
        'url': reverse('ocorrencia:homicidios'),
    }
    return render(request, template_name, context)
