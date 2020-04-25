from django import forms
from .models import Ocorrencia, Infracao, Natureza, Homicidio, PessoaOcorrencia


class OcorrenciaForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia
        fields = ('rai', 'data_do_fato', 'descricao')


class InfracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = ('pessoa', 'natureza', 'qualificacao', 'arma', 'status')


class NaturezaForm(forms.ModelForm):

    class Meta:
        model = Natureza
        fields = ('artigo', 'natureza')


class HomicidioForm(forms.ModelForm):

    class Meta:
        model = Homicidio
        fields = (
            'rai',
            'data_do_homicidio',
            'forma',
            'area_upm',
            'vitima',
            'instrumento',
            'motivacao',
            'autoria',
            'genero',
            'district',
        )


class PessoaOcorrenciaForm(forms.ModelForm):

    class Meta:
        model = PessoaOcorrencia
        fields = ('pessoa', 'ocorrencia')
