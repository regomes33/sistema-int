import json
import re
from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from localflavor.br.br_states import STATE_CHOICES

from core.models import District
from infracao.forms import InfracaoForm
from infracao.models import Arma, Infracao, Natureza
from ocorrencia.forms import PessoaOcorrenciaForm
from ocorrencia.models import Ocorrencia, PessoaOcorrencia
from pessoa.forms import (
    ComparsaForm,
    PessoaComparsaForm,
    PessoaContatoForm,
    PessoaForm,
    PessoaMinimalForm,
    PessoaVeiculoForm
)
from pessoa.models import (
    Comparsa,
    Faccao,
    Foto,
    Pessoa,
    PessoaComparsa,
    PessoaContato,
    PessoaVeiculo,
    Tatuagem
)
from utils.data import QUALIFICACAO, STATUS, TIPO
from veiculo.models import Veiculo


# @login_required
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


# @login_required
@csrf_exempt
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

    # created_by = User.objects.get(username='admin')
    if form.is_valid():
        pessoa_post = form.save(commit=False)
        # pessoa_post.created_by = created_by
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
                    # infracao_post.created_by = created_by
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
                        # veiculo_post.created_by = created_by
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
                if comparsa.get('comparsa'):
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
                        # ocorrencia_post.created_by = created_by
                        ocorrencia_post.save()
    else:
        # data = {'message': 'Erro'}
        data = form.errors
        data['status_code'] = 500

    return JsonResponse(data)


def pessoa_create_ajax(request):
    '''
    Adiciona pessoa via Ajax.
    Usado na tela ao criar Homicidio.
    '''
    form = PessoaMinimalForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form_post = form.save(commit=False)
            form_post.save()
            data = form.data
            # Turn QueryDict instance is immutable.
            data._mutable = True
            data['pk'] = form_post.pk
            data['full_name'] = ' '.join(
                filter(None, [form_post.nome, form_post.sobrenome])
            )
            return JsonResponse(data)


# @login_required
def districts(request):
    items = District.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


@csrf_exempt
def district_update(request, pk):
    district_pk = request.POST.get('district')
    if district_pk:
        district = District.objects.get(pk=district_pk)
        obj = Pessoa.objects.get(pk=pk)
        obj.district = district
        obj.save()
    response = {
        'data':
        {
            'district': obj.district.name,
            'city': obj.district.city.name,
        }
    }
    return JsonResponse(response)


# @login_required
def faccoes(request):
    items = Faccao.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


# @login_required
def status_atuais(request):
    items = STATUS
    data = [
        {
            'value': item[0],
            'text': item[1],
        }
        for item in items]
    response = {'data': data}
    return JsonResponse(response)


@csrf_exempt
def status_update(request, pk):
    status_atual = request.POST.get('status_atual')
    if status_atual:
        obj = Pessoa.objects.get(pk=pk)
        obj.status_atual = status_atual
        obj.save()
    response = {
        'data':
        {
            'value': obj.status_atual,
        }
    }
    return JsonResponse(response)


# @login_required
def naturezas(request):
    items = Natureza.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


# @login_required
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


# @login_required
def armas(request):
    items = Arma.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


# @login_required
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


# @login_required
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


# @login_required
def ocorrencias(request):
    items = Ocorrencia.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


# @login_required
def veiculos(request):
    items = Veiculo.objects.all()
    data = [item.to_dict() for item in items]
    response = {'data': data}
    return JsonResponse(response)


# @login_required
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


# @login_required
def contato_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        PessoaContato.objects.create(
            pessoa=pessoa,
            tipo=request.POST.get('tipo'),
            telefone=request.POST.get('telefone')
        )
        return JsonResponse({'data': 'OK'})


# @login_required
def contato_update(request, pk):
    contato = PessoaContato.objects.get(pk=pk)

    data = {
        'pk': contato.pk,
        'tipo': contato.tipo,
        'telefone': contato.telefone,
    }

    if request.method == 'POST':
        contato.tipo = request.POST.get('tipo')
        contato.telefone = request.POST.get('telefone')
        contato.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse(data)


# @login_required
def pessoa_veiculos(request):
    veiculos = Veiculo.objects.all()
    data = [
        {
            'pk': veiculo.pk,
            'veiculo': veiculo.placa,
        }
        for veiculo in veiculos
    ]
    return JsonResponse({'data': data})


# @login_required
def comparsas(request):
    comparsas = Comparsa.objects.all()
    data = [
        {
            'value': comparsa.pk,
            'text': comparsa.nome,
            'cpf': comparsa.cpf
        }
        for comparsa in comparsas
    ]
    return JsonResponse({'data': data})


# @login_required
@csrf_exempt
def veiculo_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        veiculo_pk = request.POST.get('veiculo_pk')
        veiculo_obj = Veiculo.objects.get(pk=veiculo_pk)

        # Salva a observação.
        observacao = request.POST.get('observacao')
        veiculo_obj.observacao = observacao
        veiculo_obj.save()

        PessoaVeiculo.objects.create(
            pessoa=pessoa,
            veiculo=veiculo_obj,
        )
        return JsonResponse({'data': 'OK'})


# @login_required
@csrf_exempt
def veiculo_update(request, pk):
    veiculo = PessoaVeiculo.objects.get(pk=pk)

    data = {
        'pk': veiculo.pk,
        'veiculo_pk': veiculo.veiculo.pk,
        'veiculo': veiculo.veiculo.placa,
        'observacao': veiculo.veiculo.observacao,
    }

    if request.method == 'POST':
        veiculo_pk = request.POST.get('veiculo_pk')
        veiculo_obj = Veiculo.objects.get(pk=veiculo_pk)
        veiculo.veiculo = veiculo_obj
        observacao = request.POST.get('observacao')
        veiculo.veiculo.observacao = observacao
        veiculo.veiculo.save()
        veiculo.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse(data)


# @login_required
@csrf_exempt
def comparsa_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)

        comparsa_pk = request.POST.get('comparsa_pk')
        comparsa = Comparsa.objects.get(pk=comparsa_pk)

        parente = request.POST.get('parente')
        if parente == 'true':
            parente = True
        else:
            parente = False
        grau_parentesco = request.POST.get('grau_parentesco')
        observacao = request.POST.get('observacao')

        _data = request.POST

        data = {'data': _data}

        # Transformando 'parente' em booleano.
        data['parente'] = parente

        PessoaComparsa.objects.create(
            pessoa=pessoa,
            comparsa=comparsa,
            parente=parente,
            grau_parentesco=grau_parentesco,
            observacao=observacao,
        )
        return JsonResponse({'data': 'OK'})


# @login_required
@csrf_exempt
def comparsa_update(request, pk):
    pessoa_comparsa = PessoaComparsa.objects.get(pk=pk)

    data = {
        'pk': pessoa_comparsa.pk,
        'comparsa_pk': pessoa_comparsa.comparsa.pk,
        'slug': pessoa_comparsa.comparsa.slug,
        'parente': pessoa_comparsa.parente,
        'grau_parentesco': pessoa_comparsa.grau_parentesco,
        'observacao': pessoa_comparsa.observacao,
    }

    if request.method == 'POST':
        comparsa_pk = request.POST.get('comparsa_pk')
        comparsa = Comparsa.objects.get(pk=comparsa_pk)

        pessoa_comparsa.comparsa = comparsa

        pessoa_comparsa.parente = request.POST.get('parente')
        if pessoa_comparsa.parente == 'true':
            pessoa_comparsa.parente = True
        else:
            pessoa_comparsa.parente = False

        pessoa_comparsa.grau_parentesco = request.POST.get('grau_parentesco')
        pessoa_comparsa.observacao = request.POST.get('observacao')

        pessoa_comparsa.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse(data)


# @login_required
@csrf_exempt
def new_comparsa_add(request):
    comparsa_data = json.loads(request.POST.get('newcomparsa'))
    form = ComparsaForm(comparsa_data)
    data = {}
    if form.is_valid():
        obj = form.save()
        data = form.data
        data['comparsa_pk'] = obj.pk
        return JsonResponse(data)
    else:
        data = {'message': 'Comparsa com este CPF já existe.', 'status': 900}
        return JsonResponse(data)
    return JsonResponse(data)


# @login_required
@csrf_exempt
def photo_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        photo = request.FILES.get('photo')
        Foto.objects.create(pessoa=pessoa, foto=photo)
        return JsonResponse({'data': 'OK'})

    return JsonResponse({})


# @login_required
@csrf_exempt
def photo_update(request, pk):
    photo = Foto.objects.get(pk=pk)

    if request.method == 'POST':
        photo.foto = request.FILES.get('photo')
        photo.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse({})


# @login_required
@csrf_exempt
def tattoo_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        tattoo = request.FILES.get('tattoo')
        Tatuagem.objects.create(pessoa=pessoa, foto=tattoo)
        return JsonResponse({'data': 'OK'})

    return JsonResponse({})


# @login_required
@csrf_exempt
def tattoo_update(request, pk):
    tattoo = Tatuagem.objects.get(pk=pk)

    if request.method == 'POST':
        tattoo.foto = request.FILES.get('tattoo')
        tattoo.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse({})


# @login_required
def pessoa_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    data = [
        {
            'pk': ocorrencia.pk,
            'ocorrencia': ocorrencia.rai,
        }
        for ocorrencia in ocorrencias
    ]
    return JsonResponse({'data': data})


# @login_required
@csrf_exempt
def ocorrencia_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        ocorrencia_pk = request.POST.get('ocorrencia_pk')
        ocorrencia_obj = Ocorrencia.objects.get(pk=ocorrencia_pk)
        PessoaOcorrencia.objects.create(
            pessoa=pessoa,
            ocorrencia=ocorrencia_obj
        )
        return JsonResponse({'data': 'OK'})


# @login_required
@csrf_exempt
def ocorrencia_update(request, pk):
    ocorrencia = PessoaOcorrencia.objects.get(pk=pk)

    data = {
        'pk': ocorrencia.pk,
        'ocorrencia_pk': ocorrencia.ocorrencia.pk,
        'ocorrencia': ocorrencia.ocorrencia.rai,
    }

    if request.method == 'POST':
        ocorrencia_pk = request.POST.get('ocorrencia_pk')
        ocorrencia_obj = Ocorrencia.objects.get(pk=ocorrencia_pk)
        ocorrencia.ocorrencia = ocorrencia_obj
        ocorrencia.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse(data)


# @login_required
@csrf_exempt
def infracao_add(request, pessoa_pk):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(pk=pessoa_pk)
        natureza_pk = ''
        arma_pk = ''
        natureza = None
        arma = None

        natureza_pk = request.POST.get('natureza_pk')
        natureza_obj = None
        if natureza_pk:
            natureza_obj = Natureza.objects.get(pk=natureza_pk)

        arma_pk = request.POST.get('arma_pk')
        arma_obj = None
        if arma_pk:
            print(arma_pk)
            arma_obj = Arma.objects.get(pk=arma_pk)

        qualificacao = request.POST.get('qualificacao')
        status = request.POST.get('status')

        if natureza_obj:
            natureza = natureza_obj

        if arma_obj:
            arma = arma_obj

        Infracao.objects.create(
            pessoa=pessoa,
            natureza=natureza,
            qualificacao=qualificacao,
            arma=arma,
            status=status,
        )
        return JsonResponse({'data': 'OK'})


# @login_required
@csrf_exempt
def infracao_update(request, pk):
    infracao = Infracao.objects.get(pk=pk)
    natureza_pk = ''
    arma_pk = ''
    if infracao.natureza:
        natureza_pk = infracao.natureza.pk
    if infracao.arma:
        arma_pk = infracao.arma.pk

    data = {
        'pk': infracao.pk,
        'natureza_pk': natureza_pk,
        'arma_pk': arma_pk,
        'qualificacao': infracao.qualificacao,
        'status': infracao.status,
    }

    if request.method == 'POST':
        natureza_pk = request.POST.get('natureza_pk')
        natureza_obj = None
        if natureza_pk:
            natureza_obj = Natureza.objects.get(pk=natureza_pk)

        arma_pk = request.POST.get('arma_pk')
        arma_obj = None
        if arma_pk:
            arma_obj = Arma.objects.get(pk=arma_pk)

        qualificacao = request.POST.get('qualificacao')
        status = request.POST.get('status')

        if natureza_obj:
            infracao.natureza = natureza_obj

        if arma_obj:
            infracao.arma = arma_obj

        infracao.qualificacao = qualificacao
        infracao.status = status
        infracao.save()
        return JsonResponse({'data': 'OK'})

    return JsonResponse(data)
