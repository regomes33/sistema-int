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


def pessoa_create(request):
    template_name = 'pessoa_form.html'
    return render(request, template_name)


# def validate_cpf(request):
#     cpf = request.GET.get('cpf', None)
#     data = {
#         'is_taken': Pessoa.objects.filter(cpf__iexact=cpf).exists()
#     }
#     return JsonResponse(data)

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
