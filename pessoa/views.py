from pprint import pprint

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from core.models import City, District
from ocorrencia.models import Natureza, Operacao, PessoaOcorrencia
from utils.data import STATUS

from .forms import ComparsaForm, PessoaForm
from .mixins import PessoaSomenteMixin, SearchMixin
from .models import Comparsa, Faccao, Pessoa


class PessoasList(LRM, PessoaSomenteMixin, SearchMixin, ListView):
    model = Pessoa
    template_name = 'pessoas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PessoasList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Pessoas'
        items_total = Pessoa.objects.\
            filter(vitima=False)\
            .values_list('id', flat=True).count()
        context['items_total'] = items_total

        # Dados para popular os dropdown dos filtros
        context['status_atuais'] = [
            {'value': item[0], 'text': item[1]}
            for item in STATUS
        ]

        context['naturezas'] = Natureza.objects.values(
            value=F('pk'),
            text=F('natureza')
        )
        context['operacoes'] = Operacao.objects.values(
            value=F('pk'),
            text=F('operacao')
        )

        context['bairros'] = District.objects.values(
            value=F('pk'),
            text=F('name')
        )

        context['cidades'] = City.objects.values(
            value=F('pk'),
            text=F('name')
        )

        context['faccoes'] = Faccao.objects.values(
            value=F('pk'),
            text=F('nome')
        )

        # Devolve o valor selecionado pra manter o filtro aplicado no template.
        data = self.request.GET
        filter_status_atual = data.getlist('filter_status_atual')
        filter_natureza = data.getlist('filter_natureza')
        filter_operacao=data.getlist('filter_operacao')
        filter_bairro = data.getlist('filter_bairro')
        filter_cidade = data.getlist('filter_cidade')
        filter_faccao = data.getlist('filter_faccao')

        # Devolve o valor para o template.
        if filter_status_atual:
            context['selected_status_atual'] = filter_status_atual
        if filter_natureza:
            context['selected_natureza'] = str(filter_natureza)
        if filter_operacao:
            context['selected_operacao'] = str(filter_operacao)    
        if filter_bairro:
            context['selected_bairro'] = str(filter_bairro)
        if filter_cidade:
            context['selected_cidade'] = str(filter_cidade)
        if filter_faccao:
            context['selected_faccao'] = str(filter_faccao)

        return context


@login_required
def pessoa_detail(request, slug):
    template_name = 'pessoa/pessoa_detail.html'
    obj = Pessoa.objects.get(slug=slug)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa__slug=slug)

    form_pessoa = PessoaForm(request.POST or None, instance=obj)
    context = {
        'endpoint': settings.ENDPOINT,
        'object': obj,
        'ocorrencias': ocorrencias,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoa_list'),
        'form_pessoa': form_pessoa,
    }
    return render(request, template_name, context)


@login_required
def pessoa_create(request):
    template_name = 'pessoa/pessoa_form.html'
    context = {
        'endpoint': settings.ENDPOINT,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoa_list'),
    }
    return render(request, template_name, context)


@login_required
def pessoa_update(request, slug):
    pessoa = Pessoa.objects.get(slug=slug)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(resolve_url('pessoa:pessoa_detail', pessoa.slug))


class ComparsaList(LRM, ListView):
    model = Comparsa
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ComparsaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ComparsaList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Comparsas'
        items_total = Comparsa.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context


class ComparsaCreate(LRM, CreateView):
    model = Comparsa
    form_class = ComparsaForm

    def get_context_data(self, **kwargs):
        context = super(ComparsaCreate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Comparsas'
        context['url'] = reverse('pessoa:comparsa_list')
        return context


class ComparsaUpdate(LRM, UpdateView):
    model = Comparsa
    form_class = ComparsaForm

    def get_context_data(self, **kwargs):
        context = super(ComparsaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Comparsas'
        context['url'] = reverse('pessoa:comparsa_list')
        return context
