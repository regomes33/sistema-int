from django import forms
from .models import Ocorrencia, Infracao, Natureza


class OcorrenciaForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia
        fields = '__all__'


class InfracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = '__all__'


class NaturezaForm(forms.ModelForm):

    class Meta:
        model = Natureza
        fields = '__all__'
