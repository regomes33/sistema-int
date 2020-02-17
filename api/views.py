import json
from pprint import pprint
from django.http import JsonResponse
from pessoa.models import Pessoa
from pessoa.forms import PessoaForm, PessoaVeiculoForm
from ocorrencia.models import Natureza, Arma
from ocorrencia.forms import InfracaoForm
from veiculo.models import Veiculo
from utils.data import QUALIFICACAO, STATUS


def pessoas(request):
    items = Pessoa.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def pessoa_add(request):
    # Adiciona Pessoa
    pessoa_data = json.loads(request.POST.get('pessoa'))
    form = PessoaForm(pessoa_data)
    if form.is_valid():
        pessoa_obj = form.save()
        # retorna dados serializados
        data = form.data
        data['pk'] = pessoa_obj.pk

        # Adiciona Infrações
        infracoes_data = json.loads(request.POST.get('infracoes'))
        if infracoes_data:
            for infracao in infracoes_data:
                infracao_form = InfracaoForm(infracao)
                if infracao_form.is_valid():
                    infracao_post = infracao_form.save(commit=False)
                    infracao_post.pessoa = pessoa_obj
                    infracao_post.save()

        # Adiciona Veículos
        veiculos_data = json.loads(request.POST.get('veiculos'))
        if veiculos_data:
            for veiculo in veiculos_data:
                veiculo_form = PessoaVeiculoForm(veiculo)
                if veiculo_form.is_valid():
                    veiculo_post = veiculo_form.save(commit=False)
                    veiculo_post.pessoa = pessoa_obj
                    veiculo_post.save()

        return JsonResponse(data)


def naturezas(request):
    items = Natureza.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def qualificacoes(request):
    items = QUALIFICACAO
    data = [
        {
            'value': item[0],
            'text': item[1],
        }
        for item in items]
    response = {'data': data}
    return JsonResponse(response)


def armas(request):
    items = Arma.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def status(request):
    items = STATUS
    data = [
        {
            'value': item[0],
            'text': item[1],
        }
        for item in items]
    response = {'data': data}
    return JsonResponse(response)


def veiculos(request):
    items = Veiculo.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)
