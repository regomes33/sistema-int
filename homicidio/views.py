from pprint import pprint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from core.models import City
from core.models import District
from homicidio.mixins import SearchMixin
from ocorrencia.forms import OcorrenciaForm
from pessoa.forms import PessoaMinimalForm
from utils.data import FORMA
from .forms import HomicidioForm
from .models import AreaUpm
from .models import Genero
from .models import Homicidio
from .models import Motivacao


class HomicidioList(LRM, SearchMixin, ListView):
    model = Homicidio
    template_name = 'homicidios.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomicidioList, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Homicidios'
        items_total = Homicidio.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total

        # Dados para popular os dropdown dos filtros
        context['formas'] = [
            {'value': item[0], 'text': item[1]}
            for item in FORMA
        ]

        context['areas'] = AreaUpm.objects.values(
            value=F('pk'),
            text=F('area_upm')
        )

        context['motivacoes'] = Motivacao.objects.values(
            value=F('pk'),
            text=F('titulo')
        )

        context['generos'] = Genero.objects.values(
            value=F('pk'),
            text=F('genero')
        )

        context['bairros'] = District.objects.values(
            value=F('pk'),
            text=F('name')
        )

        context['cidades'] = City.objects.values(
            value=F('pk'),
            text=F('name')
        )

        # Devolve o valor selecionado pra manter o filtro aplicado no template.
        data = self.request.GET
        filter_forma = data.getlist('filter_forma')
        filter_area = data.getlist('filter_area')
        filter_motivacao = data.getlist('filter_motivacao')
        filter_genero = data.getlist('filter_genero')
        filter_bairro = data.getlist('filter_bairro')
        filter_cidade = data.getlist('filter_cidade')

        filter_data_inicial = data.get('filter_data_inicial')
        filter_data_final = data.get('filter_data_final')

        # Devolve o valor para o template.
        if filter_forma:
            context['selected_forma'] = str(filter_forma)

        if filter_area:
            context['selected_area'] = str(filter_area)

        if filter_motivacao:
            context['selected_motivacao'] = str(filter_motivacao)

        if filter_genero:
            context['selected_genero'] = str(filter_genero)

        if filter_bairro:
            context['selected_bairro'] = str(filter_bairro)

        if filter_cidade:
            context['selected_cidade'] = str(filter_cidade)

        if filter_data_inicial:
            context['selected_data_inicial'] = str(filter_data_inicial)

        if filter_data_final:
            context['selected_data_final'] = str(filter_data_final)

        return context


@login_required
def homicidio_create(request):
    form = HomicidioForm(request.POST or None)
    form_ocorrencia = OcorrenciaForm(request.POST or None)
    form_pessoa = PessoaMinimalForm(request.POST or None)
    template_name = 'homicidio/homicidio_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            vitima = Homicidio.objects.filter(
                vitima=form.data.get('vitima')).first()
            if vitima:
                msg_error = 'Já existe um homicídio para esta vítima.'
                messages.error(request, msg_error)
                return HttpResponseRedirect(reverse('homicidio:homicidio_list'))
            # Transforma a pessoa em vítima
            new_form.vitima.vitima = True
            new_form.vitima.save()
            new_form.save()
            return HttpResponseRedirect(reverse('homicidio:homicidio_list'))

    context = {
        'form': form,
        'form_ocorrencia': form_ocorrencia,
        'form_pessoa': form_pessoa,
        'model_name_plural': 'Homicidios',
        'url': reverse('homicidio:homicidio_list'),
    }
    return render(request, template_name, context)


class HomicidioUpdate(LRM, UpdateView):
    model = Homicidio
    template_name = 'homicidio/homicidio_form.html'
    form_class = HomicidioForm

    def get_context_data(self, **kwargs):
        context = super(HomicidioUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Homicidios'
        context['url'] = reverse('homicidio:homicidio_list')
        context['form_ocorrencia'] = OcorrenciaForm(self.request.POST or None)
        return context
