
from pessoa.models import *
from django import forms


class PessoaFotoForm(forms.ModelForm):
    class Meta:
        model = PessoaFoto
        fields = ['fotopessoa']
        template_name = 'pessoa_form.html'


class PessoaForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF', required=True)

    nome = forms.CharField(label='Nome', required=True)
    sobrenome = forms.CharField(label='Sobre Nome', required=True)

    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'apelido', 'mae', 'pai', 'cpf']




class PessoaContaForm(forms.ModelForm):
    class Meta:
        model = PessoaContato
        fields = ['categoria', 'contato']


class PessoaEndereForm(forms.ModelForm):
    class Meta:
        model = PessoaEndereco
        fields = ['endereco', 'complemento', 'cidade', 'estado', 'pais']


class ComparsasForm(forms.ModelForm):
    class Meta:
        model = Comparsas
        fields = ['comparsas', ]


class TatuagemForm(forms.ModelForm):
    class Meta:
        model = Tatuagem
        fields = ['fototatuagem', 'descricaotatuagem']
