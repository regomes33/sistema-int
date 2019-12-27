from django.db import IntegrityError, transaction
from django.forms import modelformset_factory
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from django.contrib import messages


# Create your views here.

def pessoaCadastro(request):
    # form_pessoa = PessoaForm()
    form_pessoa = PessoaForm()

    form_contato = PessoaContatoFormSet(prefix='pessoa_contato')
    form_comparsa = ComparsaFormSet(prefix='comparsa')
    form_endereco = PessoaEnderecoFormSet(prefix='pessoa_endereco')
    form_foto = PessoaFotoFormSet(prefix='pessoa_foto')
    form_tatuagem = TatuagemFormFormSet(prefix='pessoa_tatuagem')

    if (request.method == 'POST'):
        form_cad_pessoa = PessoaForm(request.POST)

        if form_cad_pessoa.is_valid():
            objeto_pessoa = form_cad_pessoa.save()

            if objeto_pessoa.id is not None:

                ''' Dados de contato da Pessoa '''
                form_cad_pessoa_contato = PessoaContatoFormSet(
                    request.POST, prefix='pessoa_contato')

                for contato in form_cad_pessoa_contato:
                    objeto_pessoa_contato = contato.save(commit=False)
                    objeto_pessoa_contato.pessoa = objeto_pessoa

                    # print(f'Nome:
                    # {objeto_pessoa_contato.pessoa.getNomeCompleto} - Contato
                    # ({objeto_pessoa_contato.categoria}):
                    # {objeto_pessoa_contato.contato}')
                    objeto_pessoa_contato.save()

                ''' Dados de documento da Pessoa '''

                # print(f'Nome:
                # {objeto_pessoa_documento.pessoa.getNomeCompleto} - Documento
                # ({objeto_pessoa_documento.categoria}):
                # {objeto_pessoa_documento.documento}')

                ''' Dados de endereço da Pessoa '''
                form_cad_pessoa_endereco = PessoaEnderecoFormSet(
                    request.POST, prefix='pessoa_endereco')

                for endereco in form_cad_pessoa_endereco:
                    objeto_pessoa_endereco = endereco.save(commit=False)
                    objeto_pessoa_endereco.pessoa = objeto_pessoa

                    # print(f'Nome:
                    # {objeto_pessoa_endereco.pessoa.getNomeCompleto} -
                    # Endereço: {objeto_pessoa_endereco.endereco}')
                    objeto_pessoa_endereco.save()

                ''' Dados do comparsa '''
                form_cad_pessoa_comparsa = ComparsaFormSet(
                    request.POST, prefix='comparsa')

                for comparsa in form_cad_pessoa_comparsa:
                    objeto_pessoa_comparsa = comparsa.save(commit=False)
                    objeto_pessoa_comparsa.pessoa = objeto_pessoa

                    # print(f'Nome:
                    # {objeto_pessoa_comparsa.pessoa.getNomeCompleto} -
                    # Comparsa: {objeto_pessoa_comparsa.comparsas}')

                    objeto_pessoa_comparsa.save()

                '''Cadastro de Fotos'''

                form_cad_pessoa_foto = PessoaFotoFormSet(
                    request.POST, request.FILES, prefix='pessoa_foto')
                for foto in form_cad_pessoa_foto:
                    objeto_pessoa_foto = foto.save(commit=False)
                    objeto_pessoa_foto.pessoa = objeto_pessoa

                    objeto_pessoa_foto.save()

                form_cad_pessoa_tatuagem = TatuagemFormFormSet(
                    request.POST, request.FILES, prefix='pessoa_tatuagem')
                for fototatuagem in form_cad_pessoa_tatuagem:
                    objeto_pessoa_fototatuagem = fototatuagem.save(
                        commit=False)
                    objeto_pessoa_fototatuagem.pessoa = objeto_pessoa

                    objeto_pessoa_fototatuagem.save()
        messages.success(request, 'Salvo com sucesso!!')
    return render(request, 'pessoa_form.html', {'form_foto': form_foto,
                                                'form_pessoa': form_pessoa,

                                                'form_contato': form_contato,
                                                'form_endereco': form_endereco,
                                                'form_comparsa': form_comparsa,
                                                'form_tatuagem': form_tatuagem, })


def validate_cpf(request):
    cpf = request.GET.get('cpf', None)
    data = {
        'is_taken': Pessoa.objects.filter(cpf__iexact=cpf).exists()
    }
    return JsonResponse(data)


def mesagem(request):
    nome= request.Get.get('nome')
    if request.method == 'POST':
        if nome.length > 3:
            msg_sucess = 'Cadastrado com sucesso.'
            messages.success(request, msg_sucess)
    url = 'pessoa_form.html'
    return HttpResponseRedirect(reverse(url))
