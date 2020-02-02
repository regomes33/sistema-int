from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import VeiculoForm
from .models import Veiculo


def veiculos(request):
    template_name = 'veiculos.html'
    object_list = Veiculo.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def veiculo_create(request):
    form = VeiculoForm(request.POST or None)
    template_name = 'veiculo_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculo:veiculos'))

    context = {'form': form}
    return render(request, template_name, context)
