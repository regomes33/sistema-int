from django.shortcuts import render
from django.urls import reverse

from .forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# Create your views here.


def infracaoCadastro(request):
    form_infracao = infracaoForm()
    form_modusoperandi=ModusoperandiFormSet(prefix='modus_operandi')
    form_ocorrencia=OcorrenciasFormSet(prefix='ocorrencia')


    if (request.method == 'POST'):
        form_cad_infracao = infracaoForm(request.POST)

        if form_cad_infracao.is_valid():
            objeto_infracao=form_cad_infracao.save()

            if objeto_infracao.id is not None:
                form_cad_modusoperandi=ModusoperandiFormSet(request.POST,prefix='modus_operandi')

                for modusoperandi in form_cad_modusoperandi:
                    objeto_infracao_modusoperandi=modusoperandi.save(commit=False)
                    objeto_infracao_modusoperandi.infracao=objeto_infracao
                    objeto_infracao_modusoperandi.save()

                form_card_ocorrencia=OcorrenciasFormSet(request.POST, prefix='ocorrencia')
                for ocorrencia in form_card_ocorrencia:
                    objeto_infracao_ocorrencia=ocorrencia.save(commit=False)
                    objeto_infracao_ocorrencia.infracao=objeto_infracao
                    objeto_infracao_ocorrencia.save()

        messages.success(request, 'Salvo com sucesso!!')



    return render(request, 'infracao_form.html', {'form_infracao': form_infracao,
                                                  'form_modusoperandi':form_modusoperandi,
                                                  'form_ocorrencia':form_ocorrencia})



def mesagem(request):
    dataDoFato= request.Get.get('dataDoFato')
    if request.method == 'POST':
        if dataDoFato.length > 3:
            msg_sucess = 'Cadastrado com sucesso.'
            messages.success(request, msg_sucess)
    url = 'infracao_form.html'
    return HttpResponseRedirect(reverse(url))



