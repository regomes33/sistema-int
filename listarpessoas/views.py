from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.utils.text import slugify

from .forms import *


# Create your views here.
def listarPessoas(request):
    search = request.GET.get('search')
    context = {}
    pessoas = Pessoa.objects.all()
    pessoafotos = PessoaFoto.objects.all()
    if search:
        pessoas = pessoas.filter(nome__icontains=search)
    context['pessoas'] = pessoas
    context['pessoafotos'] = pessoafotos

    return render(request, 'listarpessoas.html', context)


def descricao_pessoa(request, id):
    descricao = get_object_or_404(Pessoa, pk=id)
    descricao1 = get_object_or_404(PessoaFoto, pk=id)
    descricao_contato = get_object_or_404(PessoaContato, pk=id)
    descricao_endereco = get_object_or_404(PessoaEndereco, pk=id)

    return render(request, 'descricao_pessoa.html', {'descricao': descricao,
                                                     'descricao1': descricao1,
                                                     "descricao_contato": descricao_contato,
                                                     "descricao_endereco": descricao_endereco})


def editar_pessoa(request, id):
    data = {}
    editarpessoa = get_object_or_404(Pessoa, pk=id)
    formeditarpessoa = PessoaForm(request.POST or None, instance=editarpessoa)
    data['editarpessoa'] = editarpessoa
    data['formeditarpessoa'] = formeditarpessoa

    if request.method == 'POST':
        if formeditarpessoa.is_valid():
            formeditarpessoa.save()

    return render(request, 'editar_pessoa.html', data)


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        pessoas = Pessoa.objects.all()
        pessoasfotos = PessoaFoto.objects.all()
        params = {
            'pessoas': pessoas,
            'pessoasfotos': pessoasfotos,
            'request': request,
        }
        return Render.render('relatorio.html', params, 'pessoas-cadastradas_pdf')


def person_detail_pdf(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    params = {
        'pessoa': pessoa,
        'request': request,
    }
    filename = f'relatorio_pdf_{slugify(pessoa)}'
    return Render.render('relatorio_detail.html', params, filename)


def validate_editar(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)
    mae = request.GET.get('mae', None)
    pai = request.GET.get('pai', None)
    cpf = request.GET.get('cpf', None)

    data = {
        'is_taken': Pessoa.objects.filter(cpf__iexact=cpf).exists()

    }
    return JsonResponse(data)
