from django import forms
from .models import Infracao, Natureza


class InfracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = ('pessoa', 'natureza', 'qualificacao', 'arma', 'status')


class NaturezaForm(forms.ModelForm):

    class Meta:
        model = Natureza
        fields = ('artigo', 'natureza')
