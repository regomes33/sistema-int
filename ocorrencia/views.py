import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from pessoa.forms import PessoaMinimalForm
from .forms import OcorrenciaForm, InfracaoForm, NaturezaForm, HomicidioForm
from .models import Ocorrencia, Infracao, Natureza, Homicidio, AreaUpm
from .mixins import SearchMixin


class OcorrenciaList(LRM, ListView):
    model = Ocorrencia
    template_name = 'ocorrencias.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(OcorrenciaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(rai__icontains=search) |
                Q(descricao__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Ocorrências'
        return context


@login_required
def ocorrencia(request, slug):
    template_name = 'ocorrencia.html'
    obj = Ocorrencia.objects.get(slug=slug)
    context = {
        'object': obj,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencias'),
    }
    return render(request, template_name, context)


@login_required
def ocorrencia_create(request):
    form = OcorrenciaForm(request.POST or None)
    template_name = 'ocorrencia_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:ocorrencias'))

    context = {
        'form': form,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencias'),
    }
    return render(request, template_name, context)


def ocorrencia_create_ajax(request):
    form = OcorrenciaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form_post = form.save(commit=False)
            form_post.save()
            data = form.data
            # Turn QueryDict instance is immutable.
            data._mutable = True
            data['pk'] = form_post.pk
            return JsonResponse(data)


class OcorrenciaUpdate(LRM, UpdateView):
    model = Ocorrencia
    template_name = 'ocorrencia_form.html'
    form_class = OcorrenciaForm

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Ocorrências'
        context['url'] = reverse('ocorrencia:ocorrencias')
        return context


class InfracaoList(LRM, ListView):
    model = Infracao
    template_name = 'infracoes.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(InfracaoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(natureza__natureza__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(InfracaoList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Infrações'
        return context


@login_required
def infracao_create(request):
    form = InfracaoForm(request.POST or None)
    template_name = 'infracao_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:infracoes'))

    context = {
        'form': form,
        'model_name_plural': 'Infrações',
        'url': reverse('ocorrencia:infracoes'),
    }
    return render(request, template_name, context)


class InfracaoUpdate(LRM, UpdateView):
    model = Infracao
    template_name = 'infracao_form.html'
    form_class = InfracaoForm

    def get_context_data(self, **kwargs):
        context = super(InfracaoUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Infrações'
        context['url'] = reverse('ocorrencia:infracoes')
        return context


class NaturezaList(LRM, ListView):
    model = Natureza
    template_name = 'naturezas.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(NaturezaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(natureza__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NaturezaList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Naturezas'
        return context


@login_required
def natureza_create(request):
    form = NaturezaForm(request.POST or None)
    template_name = 'natureza_form.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ocorrencia:naturezas'))

    context = {
        'form': form,
        'model_name_plural': 'Naturezas',
        'url': reverse('ocorrencia:naturezas'),
    }
    return render(request, template_name, context)


class NaturezaUpdate(LRM, UpdateView):
    model = Natureza
    template_name = 'natureza_form.html'
    form_class = NaturezaForm

    def get_context_data(self, **kwargs):
        context = super(NaturezaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Naturezas'
        context['url'] = reverse('ocorrencia:naturezas')
        return context


@login_required
def homicidios(request):
    template_name = 'homicidios.html'
    object_list = Homicidio.objects.all()


class HomicidioList(LRM, ListView, SearchMixin):
    model = Homicidio
    template_name = 'homicidios.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HomicidioList, self).get_queryset()

        # Retorna somente as vítimas.
        queryset = queryset.filter(vitima__vitima=True)

        filter_forma = self.request.GET.get('filter_forma')
        filter_area_upm = self.request.GET.get('filter_area_upm')
        filter_motivacao = self.request.GET.get('filter_motivacao')
        filter_bairro = self.request.GET.get('filter_bairro')
        if filter_area_upm:
            queryset = queryset.filter(area_upm__pk=filter_area_upm)

        if filter_motivacao:
            queryset = queryset.filter(motivacao__titulo=filter_motivacao)
        
        if filter_forma:
            queryset = queryset.filter(forma=filter_forma)

        if filter_bairro:
            queryset = queryset.filter(district=filter_bairro)

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(forma__icontains=search) |
                Q(vitima__nome__icontains=search) |
                Q(vitima__sobrenome__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomicidioList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Homicidios'
        context['area_upms'] = AreaUpm.objects.values_list('pk', 'area_upm')
        formas = Homicidio.objects.values_list(
            'forma', flat=True)
        context['formas'] = sorted(
            set([forma for forma in formas if forma]))

        motivacoes = Homicidio.objects.values_list(
            'motivacao', flat=True)
        context['motivacoes'] = sorted(
            set([motivacao for motivacao in motivacoes if motivacao]))

        bairros = Homicidio.objects.values_list(
            'district', flat=True)
        context['bairros'] = sorted(
            set([bairro for bairro in bairros if bairro]))

 # Devolve o valor selecionado pra manter o filtro aplicado no template.

        filter_forma = self.request.GET.get('filter_forma')
        filter_area_upm = self.request.GET.get('filter_area_upm')
        filter_motivacao = self.request.GET.get('filter_motivacao')
        filter_bairro = self.request.GET.get('filter_bairro')

        if filter_forma:
            context['selected_forma'] = str(filter_forma)

        if filter_area_upm:
            context['selected_area_upm'] = str(filter_area_upm)

        if filter_motivacao:
            context['selected_motivacao'] = str(filter_motivacao)

        if filter_bairro:
            context['selected_bairro'] = str(filter_bairro)

        return context


@login_required
def homicidio_create(request):
    form = HomicidioForm(request.POST or None)
    form_ocorrencia = OcorrenciaForm(request.POST or None)
    form_pessoa = PessoaMinimalForm(request.POST or None)
    template_name = 'homicidio_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            # Transforma a pessoa em vítima
            new_form.vitima.vitima = True
            new_form.vitima.save()
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:homicidios'))

    context = {
        'form': form,
        'form_ocorrencia': form_ocorrencia,
        'form_pessoa': form_pessoa,
        'model_name_plural': 'Homicidios',
        'url': reverse('ocorrencia:homicidios'),
    }
    return render(request, template_name, context)


class HomicidioUpdate(LRM, UpdateView):
    model = Homicidio
    template_name = 'homicidio_form.html'
    form_class = HomicidioForm

    def get_context_data(self, **kwargs):
        context = super(HomicidioUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Homicidios'
        context['url'] = reverse('ocorrencia:homicidios')
        context['form_ocorrencia'] = OcorrenciaForm(self.request.POST or None)
        return context
