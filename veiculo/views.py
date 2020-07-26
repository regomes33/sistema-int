from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from .forms import ModeloForm, VeiculoForm
from .models import Modelo, Veiculo


class VeiculoList(LRM, ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(VeiculoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(placa__icontains=search) |
                Q(modelo__modelo__icontains=search) |
                Q(cor__cor__icontains=search) |
                Q(observacao__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(VeiculoList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Veículos'
        items_total = Veiculo.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context


@login_required
def veiculo_create(request):
    form = VeiculoForm(request.POST or None)
    template_name = 'veiculo/veiculo_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculo:veiculo_list'))

    context = {
        'form': form,
        'model_name_plural': 'Veículos',
        'url': reverse('veiculo:veiculo_list'),
    }
    return render(request, template_name, context)


class VeiculoUpdate(LRM, UpdateView):
    model = Veiculo
    template_name = 'veiculo/veiculo_form.html'
    form_class = VeiculoForm

    def get_context_data(self, **kwargs):
        context = super(VeiculoUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Veículos'
        context['url'] = reverse('veiculo:veiculo_list')
        return context


class ModeloList(LRM, ListView):
    model = Modelo
    template_name = 'modelos.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ModeloList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(modelo__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ModeloList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Modelos'
        items_total = Modelo.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context


@login_required
def modelo_create(request):
    form = ModeloForm(request.POST or None)
    template_name = 'veiculo/modelo_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('veiculo:modelo_list'))

    context = {
        'form': form,
        'model_name_plural': 'Modelos',
        'url': reverse('veiculo:modelo_list'),
    }
    return render(request, template_name, context)


class ModeloUpdate(LRM, UpdateView):
    model = Modelo
    template_name = 'veiculo/modelo_form.html'
    form_class = ModeloForm

    def get_context_data(self, **kwargs):
        context = super(ModeloUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Modelos'
        context['url'] = reverse('veiculo:modelo_list')
        return context
