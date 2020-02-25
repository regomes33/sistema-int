import json
from pprint import pprint
from django.http import JsonResponse
from localflavor.br.br_states import STATE_CHOICES
from pessoa.models import Pessoa, Faccao, PessoaFoto
from pessoa.forms import PessoaForm, PessoaContatoForm, PessoaVeiculoForm
from ocorrencia.models import Natureza, Arma, Ocorrencia
from ocorrencia.forms import InfracaoForm, PessoaOcorrenciaForm
from veiculo.models import Veiculo
from utils.data import QUALIFICACAO, STATUS, TIPO


def pessoas(request):
    items = Pessoa.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def pessoa_add(request):
    # Adiciona Pessoa
    pessoa_data = json.loads(request.POST.get('pessoa'))
    form = PessoaForm(pessoa_data)
    created_by = request.user
    if form.is_valid():
        pessoa_post = form.save(commit=False)
        pessoa_post.created_by = created_by
        pessoa_post.save()
        # retorna dados serializados
        data = form.data
        data['pk'] = pessoa_post.pk

        # Adiciona Fotos
        for photo in request.FILES.values():
            PessoaFoto.objects.create(pessoa=pessoa_post, fotopessoa=photo)

        # Adiciona Infrações
        infracoes_data = json.loads(request.POST.get('infracoes'))
        if infracoes_data:
            for infracao in infracoes_data:
                infracao_form = InfracaoForm(infracao)
                if infracao_form.is_valid():
                    infracao_post = infracao_form.save(commit=False)
                    infracao_post.pessoa = pessoa_post
                    infracao_post.save()

        # Adiciona Veículos
        veiculos_data = json.loads(request.POST.get('veiculos'))
        if veiculos_data:
            for veiculo in veiculos_data:
                if veiculo.get('veiculo'):
                    veiculo_form = PessoaVeiculoForm(veiculo)
                    if veiculo_form.is_valid():
                        veiculo_post = veiculo_form.save(commit=False)
                        veiculo_post.pessoa = pessoa_post
                        veiculo_post.save()

        # Adiciona Contatos
        contatos_data = json.loads(request.POST.get('contatos'))
        if contatos_data:
            for contato in contatos_data:
                if contato.get('telefone'):
                    contato_form = PessoaContatoForm(contato)
                    if contato_form.is_valid():
                        contato_post = contato_form.save(commit=False)
                        contato_post.pessoa = pessoa_post
                        contato_post.save()

        # Adiciona Ocorrências
        ocorrencias_data = json.loads(request.POST.get('ocorrencias'))
        if ocorrencias_data:
            for ocorrencia in ocorrencias_data:
                if ocorrencia.get('ocorrencia'):
                    ocorrencia_form = PessoaOcorrenciaForm(ocorrencia)
                    if ocorrencia_form.is_valid():
                        ocorrencia_post = ocorrencia_form.save(commit=False)
                        ocorrencia_post.pessoa = pessoa_post
                        ocorrencia_post.save()

        return JsonResponse(data)


def faccoes(request):
    items = Faccao.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


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


def tipo_telefone(request):
    items = TIPO
    data = [
        {
            'value': item[0],
            'text': item[1],
        }
        for item in items]
    response = {'data': data}
    return JsonResponse(response)


def ocorrencias(request):
    items = Ocorrencia.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def veiculos(request):
    items = Veiculo.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def ufs(request):
    items = STATE_CHOICES
    data = [
        {
            'value': item[0],
            'text': item[1],
        }
        for item in items]
    response = {'data': data}
    return JsonResponse(response)
