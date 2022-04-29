from django import forms

from .models import Infracao, Natureza, Operacao


class InfracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = ('pessoa', 'natureza', 'operacao', 'qualificacao', 'arma')


class NaturezaForm(forms.ModelForm):

    class Meta:
        model = Natureza
        fields = ('artigo', 'natureza')


class OperacaoForm(forms.ModelForm):

    class Meta:
        model = Operacao
        fields = ('operacao', 'descricao')
