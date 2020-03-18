import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView
from pessoa.forms import PessoaMinimalForm
from .forms import OcorrenciaForm, InfracaoForm, NaturezaForm, HomicidioForm
from .models import Ocorrencia, Infracao, Natureza, Homicidio


@login_required
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


@login_required
def ocorrencia(request, slug):
    template_name = 'ocorrencia.html'
    obj = Ocorrencia.objects.get(slug=slug)
    context = {
        'object': obj,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencias'),
    }
    return render(request, template_name, context)


@login_required
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


def ocorrencia_create_ajax(request):
    form = OcorrenciaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form_post = form.save(commit=False)
            form_post.save()
            data = form.data
            # Turn QueryDict instance is immutable.
            data._mutable = True
            data['pk'] = form_post.pk
            return JsonResponse(data)


class OcorrenciaUpdate(LRM, UpdateView):
    model = Ocorrencia
    template_name = 'ocorrencia_form.html'
    form_class = OcorrenciaForm


@login_required
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


@login_required
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


class InfracaoUpdate(LRM, UpdateView):
    model = Infracao
    template_name = 'infracao_form.html'
    form_class = InfracaoForm


@login_required
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


@login_required
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


class NaturezaUpdate(LRM, UpdateView):
    model = Natureza
    template_name = 'natureza_form.html'
    form_class = NaturezaForm


@login_required
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


@login_required
def homicidio_create(request):
    form = HomicidioForm(request.POST or None)
    form_ocorrencia = OcorrenciaForm(request.POST or None)
    form_pessoa = PessoaMinimalForm(request.POST or None)
    template_name = 'homicidio_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:homicidios'))

    context = {
        'form': form,
        'form_ocorrencia': form_ocorrencia,
        'form_pessoa': form_pessoa,
        'model_name_plural': 'Homicidios',
        'url': reverse('ocorrencia:homicidios'),
    }
    return render(request, template_name, context)


class HomicidioUpdate(LRM, UpdateView):
    model = Homicidio
    template_name = 'homicidio_form.html'
    form_class = HomicidioForm
