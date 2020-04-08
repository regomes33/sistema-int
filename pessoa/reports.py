from datetime import datetime
from django.shortcuts import render
from .models import Pessoa
from ocorrencia.models import PessoaOcorrencia


def report_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {
        'object_list': pessoas,
        'today': datetime.now().today()
    }
    template_name = 'relatorios/report_pessoas.html'
    return render(request, template_name, context)


def report_pessoa(request, slug):
    pessoa = Pessoa.objects.get(slug=slug)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa__slug=slug)
    context = {
        'object': pessoa,
        'ocorrencias': ocorrencias,
        'today': datetime.now().today(),
    }
    template_name = 'relatorios/report_pessoa.html'
    return render(request, template_name, context)
