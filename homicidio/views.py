from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from homicidio.mixins import SearchMixin
from .models import AreaUpm
from .models import Homicidio
from .models import Motivacao
from .models import Genero
from .forms import HomicidioForm
from ocorrencia.forms import OcorrenciaForm
from pessoa.forms import PessoaMinimalForm


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
        filter_data_inicial = self.request.GET.get('filter_data_inicial')
        filter_data_final = self.request.GET.get('filter_data_final')

        filter_genero = self.request.GET.get('filter_genero')
        filter_bairro = self.request.GET.get('filter_bairro')

        if filter_forma:
            queryset = queryset.filter(forma=filter_forma)

        if filter_area_upm:
            queryset = queryset.filter(area_upm__pk=filter_area_upm)

        if filter_motivacao:
            queryset = queryset.filter(motivacao=filter_motivacao)

        if filter_data_inicial and filter_data_final:
            queryset = queryset.filter(
                data_do_homicidio__range=(
                    filter_data_inicial, filter_data_final)
            )

        if filter_genero:
            queryset = queryset.filter(genero=filter_genero)

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

        motivacoes = Motivacao.objects.values_list('pk', 'titulo')
        context['motivacoes'] = sorted(
            set([motivacao for motivacao in motivacoes if motivacao]))

        generos = Genero.objects.values_list('pk', 'genero')
        context['generos'] = sorted(
            set([genero for genero in generos if genero]))

        bairros = Homicidio.objects.values_list(
            'district', flat=True)
        context['bairros'] = sorted(
            set([bairro for bairro in bairros if bairro]))

        # Devolve o valor selecionado pra manter o filtro aplicado no template.
        filter_forma = self.request.GET.get('filter_forma')
        filter_area_upm = self.request.GET.get('filter_area_upm')
        filter_motivacao = self.request.GET.get('filter_motivacao')
        filter_data_inicial = self.request.GET.get('filter_data_inicial')
        filter_data_final = self.request.GET.get('filter_data_final')
        filter_genero = self.request.GET.get('filter_genero')
        filter_bairro = self.request.GET.get('filter_bairro')

        if filter_forma:
            context['selected_forma'] = str(filter_forma)

        if filter_area_upm:
            context['selected_area_upm'] = str(filter_area_upm)

        if filter_motivacao:
            context['selected_motivacao'] = str(filter_motivacao)

        if filter_data_inicial:
            context['filter_data_inicial'] = str(filter_data_inicial)

        if filter_data_final:
            context['filter_data_inicial'] = str(filter_data_final)

        if filter_genero:
            context['selected_genero'] = str(filter_genero)

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
            vitima = Homicidio.objects.filter(
                vitima=form.data.get('vitima')).first()
            if vitima:
                msg_error = 'Já existe um homicídio para esta vítima.'
                messages.error(request, msg_error)
                return HttpResponseRedirect(reverse('ocorrencia:homicidios'))
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
