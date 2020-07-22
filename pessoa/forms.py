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
            'status_atual',
            'nascimento',
            'cpf',
            'rg',
            'cnh',
            'address',
            'address_number',
            'complement',
            'district',
            'cep',
            'country',
            'observacao',
        )


class PessoaMinimalForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'sobrenome',
        )

    def save(self, commit=True):
        instance = super(PessoaMinimalForm, self).save(commit=False)
        instance.vitima = True
        instance.save()
        return instance


class PessoaContatoForm(forms.ModelForm):

    class Meta:
        model = PessoaContato
        fields = ('pessoa', 'tipo', 'telefone')


class ComparsaForm(forms.ModelForm):

    class Meta:
        model = Comparsa
        fields = ('nome', 'cpf', 'rg', 'cnh')


class PessoaVeiculoForm(forms.ModelForm):

    class Meta:
        model = PessoaVeiculo
        fields = ('pessoa', 'veiculo')
