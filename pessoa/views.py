from pprint import pprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views.generic import ListView
from core.models import City
from core.models import District
from ocorrencia.models import PessoaOcorrencia, Natureza
from utils.data import STATUS
from .forms import PessoaForm
from .mixins import PessoaSomenteMixin, SearchMixin
from .models import Pessoa, Faccao


class PessoasList(LRM, PessoaSomenteMixin, SearchMixin, ListView):
    model = Pessoa
    template_name = 'pessoas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PessoasList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Pessoas'
        # context['pessoas_total'] = Pessoa.objects.values_list('id', flat=True).count()

        # Dados para popular os dropdown dos filtros
        context['status_atuais'] = [
            {'value': item[0], 'text': item[1]}
            for item in STATUS
        ]

        context['naturezas'] = Natureza.objects.values(
            value=F('pk'),
            text=F('natureza')
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
        filter_status_atual = self.request.GET.get('filter_status_atual')
        filter_natureza = self.request.GET.get('filter_natureza')
        filter_bairro = self.request.GET.get('filter_bairro')
        filter_cidade = self.request.GET.get('filter_cidade')
        filter_faccao = self.request.GET.get('filter_faccao')

        # Devolve o valor para o template.
        if filter_status_atual:
            context['selected_status_atual'] = filter_status_atual
        if filter_natureza:
            context['selected_natureza'] = str(filter_natureza)
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
            return HttpResponseRedirect(resolve_url('pessoa:pessoa', pessoa.slug))
