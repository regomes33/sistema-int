from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView

from ocorrencia.models import PessoaOcorrencia

from .mixins import PessoaSomenteMixin, SearchMixin
from .models import Pessoa


class ReportPessoasList(PessoaSomenteMixin, SearchMixin, ListView):
    model = Pessoa
    template_name = 'reports/report_pessoa_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReportPessoasList, self).get_context_data(**kwargs)
        context['today'] = datetime.now().today()
        return context


def report_pessoa(request, slug):
    pessoa = Pessoa.objects.get(slug=slug)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa__slug=slug)
    context = {
        'object': pessoa,
        'ocorrencias': ocorrencias,
        'today': datetime.now().today(),
    }
    template_name = 'reports/report_pessoa_detail.html'
    return render(request, template_name, context)
