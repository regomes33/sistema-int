from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView
from .forms import VeiculoForm, ModeloForm
from .models import Veiculo, Modelo


@login_required
def veiculos(request):
    template_name = 'veiculos.html'
    object_list = Veiculo.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(placa__icontains=search) |
            Q(modelo__modelo__icontains=search) |
            Q(cor__cor__icontains=search)
        )

    context = {
        'object_list': object_list,
        'model_name_plural': 'Veículos',
    }
    return render(request, template_name, context)


@login_required
def veiculo_create(request):
    form = VeiculoForm(request.POST or None)
    template_name = 'veiculo_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculo:veiculos'))

    context = {
        'form': form,
        'model_name_plural': 'Veículos',
        'url': reverse('veiculo:veiculos'),
    }
    return render(request, template_name, context)


class VeiculoUpdate(LRM, UpdateView):
    model = Veiculo
    template_name = 'veiculo_form.html'
    form_class = VeiculoForm


@login_required
def modelos(request):
    template_name = 'modelos.html'
    object_list = Modelo.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(modelo__icontains=search)

    context = {
        'object_list': object_list,
        'model_name_plural': 'Modelos',
    }
    return render(request, template_name, context)


@login_required
def modelo_create(request):
    form = ModeloForm(request.POST or None)
    template_name = 'modelo_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculo:modelos'))

    context = {
        'form': form,
        'model_name_plural': 'Modelos',
        'url': reverse('veiculo:modelos'),
    }
    return render(request, template_name, context)


class ModeloUpdate(LRM, UpdateView):
    model = Modelo
    template_name = 'modelo_form.html'
    form_class = ModeloForm
