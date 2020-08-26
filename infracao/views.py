from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from .forms import InfracaoForm, NaturezaForm,OperacaoForm
from .models import Infracao, Natureza, Operacao


class InfracaoList(LRM, ListView):
    model = Infracao
    template_name = 'infracoes.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(InfracaoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(pessoa__nome__icontains=search) |
                Q(pessoa__sobrenome__icontains=search) |
                Q(pessoa__apelido__icontains=search) |
                Q(natureza__natureza__icontains=search) |
                Q(operacao__operacao__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(InfracaoList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Infrações'
        items_total = Infracao.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context


@login_required
def infracao_create(request):
    form = InfracaoForm(request.POST or None)
    template_name = 'infracao/infracao_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('infracao:infracao_list'))

    context = {
        'form': form,
        'model_name_plural': 'Infrações',
        'url': reverse('infracao:infracao_list'),
    }
    return render(request, template_name, context)


class InfracaoUpdate(LRM, UpdateView):
    model = Infracao
    template_name = 'infracao/infracao_form.html'
    form_class = InfracaoForm

    def get_context_data(self, **kwargs):
        context = super(InfracaoUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Infrações'
        context['url'] = reverse('infracao:infracao_list')
        return context


class NaturezaList(LRM, ListView):
    model = Natureza
    template_name = 'naturezas.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(NaturezaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(natureza__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NaturezaList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Naturezas'
        items_total = Natureza.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context

class NaturezaUpdate(LRM, UpdateView):
    model = Natureza
    template_name = 'infracao/natureza_form.html'
    form_class = NaturezaForm

    def get_context_data(self, **kwargs):
        context = super(NaturezaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Naturezas'
        context['url'] = reverse('infracao:natureza_list')
        return context

@login_required
def natureza_create(request):
    form = NaturezaForm(request.POST or None)
    template_name = 'infracao/natureza_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('infracao:natureza_list'))

    context = {
        'form': form,
        'model_name_plural': 'Naturezas',
        'url': reverse('infracao:natureza_list'),
    }
    return render(request, template_name, context)


class NaturezaUpdate(LRM, UpdateView):
    model = Natureza
    template_name = 'infracao/natureza_form.html'
    form_class = NaturezaForm

    def get_context_data(self, **kwargs):
        context = super(NaturezaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Naturezas'
        context['url'] = reverse('infracao:natureza_list')
        return context
    
class OperacaoList(LRM, ListView):
    model = Operacao
    template_name = 'operacao.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(OperacaoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(operacao__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(OperacaoList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Operacoes'
        items_total = Operacao.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context    

@login_required
def operacao_create(request):
    form = OperacaoForm(request.POST or None)
    template_name = 'infracao/operacao_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('infracao:operacao_list'))

    context = {
        'form': form,
        'model_name_plural': 'Operacoes',
        'url': reverse('infracao:operacao_list'),
    }
    return render(request, template_name, context)

class OperacaoUpdate(LRM, UpdateView):
    model = Operacao
    template_name = 'infracao/operacao_form.html'
    form_class = OperacaoForm

    def get_context_data(self, **kwargs):
        context = super(OperacaoUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Operações'
        context['url'] = reverse('infracao:operacao_list')
        return context