from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import VeiculoForm, ModeloForm
from .models import Veiculo, Modelo


def veiculos(request):
    template_name = 'veiculos.html'
    object_list = Veiculo.objects.all()
    context = {
        'object_list': object_list,
        'model_name_plural': 'Veículos',
    }
    return render(request, template_name, context)


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


def modelos(request):
    template_name = 'modelos.html'
    object_list = Modelo.objects.all()
    context = {
        'object_list': object_list,
        'model_name_plural': 'Modelos',
    }
    return render(request, template_name, context)


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
