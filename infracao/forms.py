from django import forms
from .models import *


class infracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = ['pessoa', 'primeiranatureza', 'segundanatureza',
                  'qualificacao', 'arma_de_fogo', 'status']


class OcorrenciasForm(forms.ModelForm):

    class Meta:
        model = Ocorrencias
        fields = ['rai', 'data_do_fato', 'descricao']

#
# class crimeForm(forms.ModelForm):
#     class Meta:
#         model = Crime
#         fields = ['autor', 'vitima', 'data']
#
#
# CrimeFormSet = forms.formset_factory(crimeForm, extra=1)

# OcorrenciasFormSet = forms.formset_factory(OcorrenciasForm, extra=1)
