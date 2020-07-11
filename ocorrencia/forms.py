from django import forms
from .models import Ocorrencia, PessoaOcorrencia


class OcorrenciaForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia
        fields = ('rai', 'data_do_fato', 'descricao')


class PessoaOcorrenciaForm(forms.ModelForm):

    class Meta:
        model = PessoaOcorrencia
        fields = ('pessoa', 'ocorrencia')
