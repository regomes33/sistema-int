from django import forms
from .models import Pessoa, PessoaContato, PessoaVeiculo


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'cpf')


class PessoaContatoForm(forms.ModelForm):

    class Meta:
        model = PessoaContato
        fields = ('pessoa', 'tipo', 'telefone')


class PessoaVeiculoForm(forms.ModelForm):

    class Meta:
        model = PessoaVeiculo
        fields = ('pessoa', 'veiculo')
