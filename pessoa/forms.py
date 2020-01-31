import re
from django import forms
from .models import *

cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


class infracaoForm(forms.ModelForm):

    class Meta:
        model = Infracao
        fields = (
            'pessoa',
            'primeiranatureza',
            'segundanatureza',
            'qualificacao',
            'arma_de_fogo',
            'status'
        )


class OcorrenciasForm(forms.ModelForm):

    class Meta:
        model = Ocorrencias
        fields = ('rai', 'data_do_fato', 'descricao')


class PessoaFotoForm(forms.ModelForm):

    class Meta:
        model = PessoaFoto
        fields = ('fotopessoa',)
        template_name = 'pessoa_form.html'


class PessoaForm(forms.ModelForm):
    cpf = forms.CharField(
        label='CPF',
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Digite um CPF Valido"})
    )

    nome = forms.CharField(
        label='Nome',
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Digite o Nome: Apenas LETRAS "})
    )
    sobrenome = forms.CharField(
        label='Sobre Nome',
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Digite o Sobre Nome: Apenas LETRAS "})
    )

    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'apelido', 'mae', 'pai', 'cpf')


class PessoaContaForm(forms.ModelForm):

    class Meta:
        model = PessoaContato
        fields = ('categoria', 'contato')


class PessoaEndereForm(forms.ModelForm):

    class Meta:
        model = PessoaEndereco
        fields = ('endereco', 'complemento', 'cidade', 'estado', 'pais')


class ComparsasForm(forms.ModelForm):

    class Meta:
        model = Comparsas
        fields = ('comparsas',)


class TatuagemForm(forms.ModelForm):

    class Meta:
        model = Tatuagem
        fields = ('fototatuagem', 'descricaotatuagem')
