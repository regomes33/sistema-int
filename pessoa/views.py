from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views.generic import ListView
from .forms import PessoaForm
from .models import Pessoa, Faccao
from .mixins import PessoaSomenteMixin, SearchMixin
from ocorrencia.models import PessoaOcorrencia, Natureza


class PessoasList(LRM, PessoaSomenteMixin, SearchMixin, ListView):
    model = Pessoa
    template_name = 'pessoas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PessoasList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Pessoas'
        # context['pessoas_total'] = Pessoa.objects.values_list('id', flat=True).count()

        context['naturezas'] = Natureza.objects.values_list('pk', 'natureza')

        bairros = Pessoa.objects.values_list(
            'district', flat=True)
        context['bairros'] = sorted(
            set([bairro for bairro in bairros if bairro]))

        # cidades = Pessoa.objects.values_list('city', flat=True)
        # context['cidades'] = sorted(set([cidade for cidade in cidades if cidade]))

        context['faccoes'] = Faccao.objects.values_list('pk', 'nome')

        # Devolve o valor selecionado pra manter o filtro aplicado no template.
        filter_natureza = self.request.GET.get('filter_natureza')
        filter_bairro = self.request.GET.get('filter_bairro')
        filter_faccao = self.request.GET.get('filter_faccao')
        filter_cidade = self.request.GET.get('filter_cidade')

        if filter_natureza:
            context['selected_natureza'] = str(filter_natureza)
        if filter_bairro:
            context['selected_bairro'] = str(filter_bairro)
        if filter_faccao:
            context['selected_faccao'] = str(filter_faccao)
        if filter_cidade:
            context['selected_cidade'] = str(filter_cidade)

        return context


@login_required
def pessoa(request, slug):
    template_name = 'pessoa.html'
    obj = Pessoa.objects.get(slug=slug)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa__slug=slug)

    form_pessoa = PessoaForm(request.POST or None, instance=obj)
    context = {
        'endpoint': settings.ENDPOINT,
        'object': obj,
        'ocorrencias': ocorrencias,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoas'),
        'form_pessoa': form_pessoa,
    }
    return render(request, template_name, context)


@login_required
def pessoa_create(request):
    template_name = 'pessoa_form.html'
    context = {
        'endpoint': settings.ENDPOINT,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoas'),
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
