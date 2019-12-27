from django import forms
from .models import *


class infracaoForm(forms.ModelForm):
    class Meta:
        model = Infracao
        fields = ['pessoa', 'natureza', 'natureza2', 'qualificacao', 'arma_de_fogo', 'status']


class ModusOperandiForm(forms.ModelForm):
    class Meta:
        model = Modusoperandi
        fields = [ 'faccao', 'funcao']


class OcorrenciasForm(forms.ModelForm):
    class Meta:
        model = Ocorrencias
        fields = ['rai', 'dataDoFato', 'descrição']

#
# class crimeForm(forms.ModelForm):
#     class Meta:
#         model = Crime
#         fields = ['autor', 'vitima', 'data']
#
#
# CrimeFormSet = forms.formset_factory(crimeForm, extra=1)

ModusoperandiFormSet = forms.formset_factory(ModusOperandiForm, extra=1)

OcorrenciasFormSet = forms.formset_factory(OcorrenciasForm, extra=1)

