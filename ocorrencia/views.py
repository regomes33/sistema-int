from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from .forms import OcorrenciaForm
from .models import Ocorrencia


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
        items_total = Ocorrencia.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        return context


@login_required
def ocorrencia_create(request):
    form = OcorrenciaForm(request.POST or None)
    template_name = 'ocorrencia/ocorrencia_form.html'

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('ocorrencia:ocorrencia_list'))

    context = {
        'form': form,
        'model_name_plural': 'Ocorrências',
        'url': reverse('ocorrencia:ocorrencia_list'),
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
    template_name = 'ocorrencia/ocorrencia_form.html'
    form_class = OcorrenciaForm

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaUpdate, self).get_context_data(**kwargs)
        context['model_name_plural'] = 'Ocorrências'
        context['url'] = reverse('ocorrencia:ocorrencia_list')
        return context
