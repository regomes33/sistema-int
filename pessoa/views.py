# import xhtml2pdf.pisa as pisa
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pessoa
from ocorrencia.models import PessoaOcorrencia


@login_required
def pessoas(request):
    template_name = 'pessoas.html'
    object_list = Pessoa.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(nome__icontains=search) |
            Q(sobrenome__icontains=search) |
            Q(apelido__icontains=search)
        )

    context = {
        'object_list': object_list,
        'model_name_plural': 'Pessoas',
    }
    return render(request, template_name, context)


@login_required
def pessoa(request, pk):
    template_name = 'pessoa.html'
    obj = Pessoa.objects.get(pk=pk)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa=pk)
    context = {
        'object': obj,
        'ocorrencias': ocorrencias,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoas'),
    }
    return render(request, template_name, context)


@login_required
def pessoa_create(request):
    template_name = 'pessoa_form.html'
    context = {
        'endpoint': settings.ENDPOINT,
        'model_name_plural': 'Pessoas',
        'url': reverse('pessoa:pessoas'),
    }
    return render(request, template_name, context)


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
