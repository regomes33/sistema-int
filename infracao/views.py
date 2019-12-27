from django.shortcuts import render
from .forms import *


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





    return render(request, 'infracao_form.html', {'form_infracao': form_infracao,
                                                  'form_modusoperandi':form_modusoperandi,
                                                  'form_ocorrencia':form_ocorrencia})
