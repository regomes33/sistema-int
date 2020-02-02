# import io
# from django.conf import settings
# from django.contrib import messages
# from django.contrib.admin.templatetags.admin_list import pagination
# from django.db import IntegrityError, transaction
# from django.forms import modelformset_factory
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404, redirect
# from django.template.loader import get_template
# from django.urls import reverse
# from django.utils.text import slugify
# from django.views.generic.base import View
# from .models import Infracao
# import xhtml2pdf.pisa as pisa
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pessoa
from ocorrencia.models import PessoaOcorrencia


def pessoas(request):
    template_name = 'pessoas.html'
    object_list = Pessoa.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def pessoa(request, pk):
    template_name = 'pessoa.html'
    obj = Pessoa.objects.get(pk=pk)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa=pk)
    context = {
        'object': obj,
        'ocorrencias': ocorrencias
    }
    return render(request, template_name, context)


# def pessoaCadastro(request):
#     # form_pessoa = PessoaForm()
#     form_pessoa = PessoaForm()

#     form_contato = PessoaContatoFormSet(prefix='pessoa_contato')
#     form_comparsa = ComparsaFormSet(prefix='comparsa')
#     form_endereco = PessoaEnderecoFormSet(prefix='pessoa_endereco')
#     form_foto = PessoaFotoFormSet(prefix='pessoa_foto')
#     form_tatuagem = TatuagemFormFormSet(prefix='pessoa_tatuagem')

#     if (request.method == 'POST'):
#         form_cad_pessoa = PessoaForm(request.POST)

#         if form_cad_pessoa.is_valid():
#             objeto_pessoa = form_cad_pessoa.save()

#             if objeto_pessoa.id is not None:

#                 ''' Dados de contato da Pessoa '''
#                 form_cad_pessoa_contato = PessoaContatoFormSet(
#                     request.POST, prefix='pessoa_contato')

#                 for contato in form_cad_pessoa_contato:
#                     objeto_pessoa_contato = contato.save(commit=False)
#                     objeto_pessoa_contato.pessoa = objeto_pessoa

#                     # print(f'Nome:
#                     # {objeto_pessoa_contato.pessoa.getNomeCompleto} - Contato
#                     # ({objeto_pessoa_contato.categoria}):
#                     # {objeto_pessoa_contato.contato}')
#                     objeto_pessoa_contato.save()

#                 ''' Dados de documento da Pessoa '''

#                 # print(f'Nome:
#                 # {objeto_pessoa_documento.pessoa.getNomeCompleto} - Documento
#                 # ({objeto_pessoa_documento.categoria}):
#                 # {objeto_pessoa_documento.documento}')

#                 ''' Dados de endereço da Pessoa '''
#                 form_cad_pessoa_endereco = PessoaEnderecoFormSet(
#                     request.POST, prefix='pessoa_endereco')

#                 for endereco in form_cad_pessoa_endereco:
#                     objeto_pessoa_endereco = endereco.save(commit=False)
#                     objeto_pessoa_endereco.pessoa = objeto_pessoa

#                     # print(f'Nome:
#                     # {objeto_pessoa_endereco.pessoa.getNomeCompleto} -
#                     # Endereço: {objeto_pessoa_endereco.endereco}')
#                     objeto_pessoa_endereco.save()

#                 ''' Dados do comparsa '''
#                 form_cad_pessoa_comparsa = ComparsaFormSet(
#                     request.POST, prefix='comparsa')

#                 for comparsa in form_cad_pessoa_comparsa:
#                     objeto_pessoa_comparsa = comparsa.save(commit=False)
#                     objeto_pessoa_comparsa.pessoa = objeto_pessoa

#                     # print(f'Nome:
#                     # {objeto_pessoa_comparsa.pessoa.getNomeCompleto} -
#                     # Comparsa: {objeto_pessoa_comparsa.comparsas}')

#                     objeto_pessoa_comparsa.save()

#                 '''Cadastro de Fotos'''

#                 form_cad_pessoa_foto = PessoaFotoFormSet(
#                     request.POST, request.FILES, prefix='pessoa_foto')
#                 for foto in form_cad_pessoa_foto:
#                     objeto_pessoa_foto = foto.save(commit=False)
#                     objeto_pessoa_foto.pessoa = objeto_pessoa

#                     objeto_pessoa_foto.save()

#                 form_cad_pessoa_tatuagem = TatuagemFormFormSet(
#                     request.POST, request.FILES, prefix='pessoa_tatuagem')
#                 for fototatuagem in form_cad_pessoa_tatuagem:
#                     objeto_pessoa_fototatuagem = fototatuagem.save(
#                         commit=False)
#                     objeto_pessoa_fototatuagem.pessoa = objeto_pessoa

#                     objeto_pessoa_fototatuagem.save()
#         messages.success(request, 'Salvo com sucesso!!')
#     return render(request, 'pessoa_form.html', {'form_foto': form_foto,
#                                                 'form_pessoa': form_pessoa,

#                                                 'form_contato': form_contato,
#                                                 'form_endereco': form_endereco,
#                                                 'form_comparsa': form_comparsa,
#                                                 'form_tatuagem': form_tatuagem, })


# def validate_cpf(request):
#     cpf = request.GET.get('cpf', None)
#     data = {
#         'is_taken': Pessoa.objects.filter(cpf__iexact=cpf).exists()
#     }
#     return JsonResponse(data)


# def mesagem(request):
#     nome = request.Get.get('nome')
#     if request.method == 'POST':
#         if nome.length > 3:
#             msg_sucess = 'Cadastrado com sucesso.'
#             messages.success(request, msg_sucess)
#     url = 'pessoa_form.html'
#     return HttpResponseRedirect(reverse(url))


# def infracaoCadastro(request):
#     form_infracao = infracaoForm()
#     form_modusoperandi = ModusoperandiFormSet(prefix='modus_operandi')
#     form_ocorrencia = OcorrenciasFormSet(prefix='ocorrencia')

#     if (request.method == 'POST'):
#         form_cad_infracao = infracaoForm(request.POST)

#         if form_cad_infracao.is_valid():
#             objeto_infracao = form_cad_infracao.save()

#             if objeto_infracao.id is not None:
#                 form_cad_modusoperandi = ModusoperandiFormSet(
#                     request.POST, prefix='modus_operandi')

#                 for modusoperandi in form_cad_modusoperandi:
#                     objeto_infracao_modusoperandi = modusoperandi.save(
#                         commit=False)
#                     objeto_infracao_modusoperandi.infracao = objeto_infracao
#                     objeto_infracao_modusoperandi.save()

#                 form_card_ocorrencia = OcorrenciasFormSet(
#                     request.POST, prefix='ocorrencia')
#                 for ocorrencia in form_card_ocorrencia:
#                     objeto_infracao_ocorrencia = ocorrencia.save(commit=False)
#                     objeto_infracao_ocorrencia.infracao = objeto_infracao
#                     objeto_infracao_ocorrencia.save()
#     messages.success(request, 'Salvo com sucesso!!')
#     return render(request, 'infracao_form.html', {'form_infracao': form_infracao,
#                                                   'form_modusoperandi': form_modusoperandi,
#                                                   'form_ocorrencia': form_ocorrencia})


# # def mesagem(request):
# #     dataDoFato = request.Get.get('dataDoFato')
# #     if request.method == 'POST':
# #         if dataDoFato.length > 3:
# #             msg_sucess = 'Cadastrado com sucesso.'
# #             messages.success(request, msg_sucess)
# #     url = 'infracao_form.html'
# #     return HttpResponseRedirect(reverse(url))


# def listarPessoas(request):
#     search = request.GET.get('search')
#     context = {}
#     pessoas = Pessoa.objects.all()
#     pessoafotos = PessoaFoto.objects.all()
#     if search:
#         pessoas = pessoas.filter(nome__icontains=search)
#     context['pessoas'] = pessoas
#     context['pessoafotos'] = pessoafotos

#     return render(request, 'listarpessoas.html', context)


# def descricao_pessoa(request, id):
#     descricao = get_object_or_404(Pessoa, pk=id)
#     descricao1 = get_object_or_404(PessoaFoto, pessoa=descricao)
#     descricao_contato = get_object_or_404(PessoaContato, pessoa=descricao)
#     descricao_endereco = get_object_or_404(PessoaEndereco, pessoa=descricao)
#     descricao_infracao = get_object_or_404(Infracao, pessoa=descricao)
#     context = {
#         'descricao': descricao,
#         'descricao1': descricao1,
#         'descricao_contato': descricao_contato,
#         'descricao_endereco': descricao_endereco,
#         'descricao_infracao': descricao_infracao
#     }
#     return render(request, 'descricao_pessoa.html', context)


# def editar_pessoa(request, id):
#     data = {}
#     editarpessoa = get_object_or_404(Pessoa, pk=id)
#     formeditarpessoa = PessoaForm(request.POST or None, instance=editarpessoa)
#     data['editarpessoa'] = editarpessoa
#     data['formeditarpessoa'] = formeditarpessoa

#     if request.method == 'POST':
#         if formeditarpessoa.is_valid():
#             formeditarpessoa.save()

#     return render(request, 'editar_pessoa.html', data)


# class Render:

#     @staticmethod
#     def render(path: str, params: dict, filename: str):
#         template = get_template(path)
#         html = template.render(params)
#         response = io.BytesIO()
#         pdf = pisa.pisaDocument(
#             io.BytesIO(html.encode("UTF-8")), response)
#         if not pdf.err:
#             response = HttpResponse(
#                 response.getvalue(), content_type='application/pdf')
#             response[
#                 'Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
#             return response
#         else:
#             return HttpResponse("Error Rendering PDF", status=400)


# class Pdf(View):

#     def get(self, request):
#         pessoas = Pessoa.objects.all()
#         pessoasfotos = PessoaFoto.objects.all()
#         params = {
#             'media': settings.BASE_DIR,
#             'pessoas': pessoas,
#             'pessoasfotos': pessoasfotos,
#             'request': request,
#         }
# return Render.render('relatorio.html', params,
# 'pessoas-cadastradas_pdf')


# def person_detail_pdf(request, pk):
#     pessoa = Pessoa.objects.get(pk=pk)
#     pessoafoto = PessoaFoto.objects.get(pk=pk)
#     pessoaendereco = PessoaEndereco.objects.get(pk=pk)
#     infracao = Infracao.objects.get(pk=pk)

#     params = {
#         'pessoafoto': pessoafoto,
#         'pessoa': pessoa,
#         'request': request,
#         'pessoaendereco': pessoaendereco,


#     }
#     filename = f'relatorio_pdf_{slugify(pessoa)}'
#     return Render.render('relatorio_detail.html', params, filename)


# def validate_editar(request):
#     nome = request.GET.get('nome', None)
#     sobrenome = request.GET.get('sobrenome', None)
#     mae = request.GET.get('mae', None)
#     pai = request.GET.get('pai', None)
#     cpf = request.GET.get('cpf', None)

#     data = {
#         'is_taken': Pessoa.objects.filter(cpf__iexact=cpf).exists()

#     }
#     return JsonResponse(data)
