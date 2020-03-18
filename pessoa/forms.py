from django import forms
from .models import Pessoa, Comparsa, PessoaContato, PessoaVeiculo


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'sobrenome',
            'apelido',
            'mae',
            'pai',
            'faccao',
            'cpf',
            'rg',
            'cnh',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'country',
        )


class PessoaMinimalForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'sobrenome',
        )


class PessoaContatoForm(forms.ModelForm):

    class Meta:
        model = PessoaContato
        fields = ('pessoa', 'tipo', 'telefone')


class PessoaComparsaForm(forms.ModelForm):

    class Meta:
        model = Comparsa
        fields = ('pessoa', 'nome', 'cpf', 'rg', 'cnh')


class PessoaVeiculoForm(forms.ModelForm):

    class Meta:
        model = PessoaVeiculo
        fields = ('pessoa', 'veiculo')
