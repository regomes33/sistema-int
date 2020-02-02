from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from .forms import VeiculoForm
from .models import Veiculo


def veiculos(request):
    template_name = 'veiculos.html'
    object_list = Veiculo.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
