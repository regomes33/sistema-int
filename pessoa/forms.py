from django import forms
from .models import Pessoa, PessoaVeiculo


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'cpf')


class PessoaVeiculoForm(forms.ModelForm):

    class Meta:
        model = PessoaVeiculo
        fields = ('pessoa', 'veiculo')
