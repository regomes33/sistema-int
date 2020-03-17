# import xhtml2pdf.pisa as pisa
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Pessoa
from .mixins import SearchMixin
from ocorrencia.models import PessoaOcorrencia


class PessoasList(LRM, SearchMixin, ListView):
    model = Pessoa
    template_name = 'pessoas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PessoasList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Pessoas'
        return context


@login_required
def pessoa(request, slug):
    template_name = 'pessoa.html'
    obj = Pessoa.objects.get(slug=slug)
    ocorrencias = PessoaOcorrencia.objects.filter(pessoa__slug=slug)
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
