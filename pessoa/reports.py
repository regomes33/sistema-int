from django.db.models import Q
from datetime import datetime
from django.shortcuts import render
from .models import Pessoa
from ocorrencia.models import PessoaOcorrencia


def report_pessoas(request):
    pessoas = Pessoa.objects.all()

    filter_natureza = request.GET.get('filter_natureza')
    filter_bairro = request.GET.get('filter_bairro')
    filter_faccao = request.GET.get('filter_faccao')
    filter_cidade = request.GET.get('filter_cidade')

    if filter_natureza:
        pessoas = pessoas.filter(Q(infracao__natureza=filter_natureza))

    if filter_bairro:
        pessoas = pessoas.filter(Q(district=filter_bairro))

    if filter_cidade:
        pessoas = pessoas.filter(Q(city=filter_cidade))

    if filter_faccao:
        pessoas = pessoas.filter(Q(faccao=filter_faccao))

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
