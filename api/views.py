import json
import re
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from localflavor.br.br_states import STATE_CHOICES
from ocorrencia.forms import InfracaoForm, PessoaOcorrenciaForm
from ocorrencia.models import Natureza, Arma, Ocorrencia
from pessoa.forms import PessoaForm, PessoaContatoForm, PessoaComparsaForm
from pessoa.forms import PessoaVeiculoForm
from pessoa.models import Pessoa, Faccao, Foto, Tatuagem
from utils.data import QUALIFICACAO, STATUS, TIPO
from veiculo.models import Veiculo


@login_required
def pessoas(request):
    items = Pessoa.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


def cpf_validate(cpf, data):
    # Retorna somente os números do CPF
    if not cpf.isdigit():
        cpf = re.sub("[-\.]", "", cpf)
    # Verifica se o CPF contém exatamente 11 digitos.
    if len(cpf) != 11:
        data = {
            'message': 'CPF deve conter 11 dígitos!',
            'status_code': 900
        }
    # Verifica se CPF já existe.
    cpf_exists = Pessoa.objects.filter(cpf=cpf)
    if cpf_exists:
        data = {
            'message': 'CPF já cadastrado!',
            'status_code': 900
        }
    return cpf, data


@login_required
def pessoa_add(request):
    # Adiciona Pessoa
    pessoa_data = json.loads(request.POST.get('pessoa'))
    form = PessoaForm(pessoa_data)

    data = {}

    _cpf = form.data.get('cpf')
    if _cpf:
        cpf, data = cpf_validate(_cpf, data)
        if data.get('status_code') == 900:
            return JsonResponse(data)

    created_by = request.user
    if form.is_valid():
        pessoa_post = form.save(commit=False)
        pessoa_post.created_by = created_by
        pessoa_post.save()
        # retorna dados serializados
        data = form.data
        data['pk'] = pessoa_post.pk
        data['status_code'] = 200

        files = request.FILES.items()
        photos, tattoos = [], []

        for name, file in files:
            if 'photo' in name:
                photos.append(file)
            if 'tattoo' in name:
                tattoos.append(file)

        # Adiciona Fotos
        for photo in photos:
            Foto.objects.create(pessoa=pessoa_post, foto=photo)

        # Adiciona Tatuagens
        for tattoo in tattoos:
            Tatuagem.objects.create(pessoa=pessoa_post, foto=tattoo)

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

        # Adiciona Comparsas
        comparsas_data = json.loads(request.POST.get('comparsas'))
        if comparsas_data:
            for comparsa in comparsas_data:
                if comparsa.get('nome'):
                    comparsa_form = PessoaComparsaForm(comparsa)
                    if comparsa_form.is_valid():
                        comparsa_post = comparsa_form.save(commit=False)
                        comparsa_post.pessoa = pessoa_post
                        comparsa_post.save()

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
    else:
        # data = {'message': 'Erro'}
        data = form.errors
        data['status_code'] = 500

    return JsonResponse(data)


@login_required
def faccoes(request):
    items = Faccao.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@login_required
def naturezas(request):
    items = Natureza.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@login_required
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


@login_required
def armas(request):
    items = Arma.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@login_required
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


@login_required
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


@login_required
def ocorrencias(request):
    items = Ocorrencia.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@login_required
def veiculos(request):
    items = Veiculo.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@login_required
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
