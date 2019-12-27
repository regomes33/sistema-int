from __future__ import unicode_literals

import re

from django import forms

from .models import *

cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


class PessoaFotoForm(forms.ModelForm):
    class Meta:
        model = PessoaFoto
        fields = ['fotopessoa']
        template_name = 'pessoa_form.html'


class PessoaForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF', required=True,
                          widget=forms.TextInput(attrs={"placeholder": "Digite um CPF Valido"}))

    nome = forms.CharField(label='', required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Digite o Nome: Apenas LETRAS "}))
    sobrenome = forms.CharField(label='', required=True,
                                widget=forms.TextInput(attrs={"placeholder": "Digite o Sobre Nome: Apenas LETRAS "}))

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


PessoaContatoFormSet = forms.formset_factory(PessoaContaForm, extra=1)

PessoaEnderecoFormSet = forms.formset_factory(PessoaEndereForm, extra=1)
PessoaFotoFormSet = forms.formset_factory(PessoaFotoForm, extra=1)
ComparsaFormSet = forms.formset_factory(ComparsasForm, extra=1)
TatuagemFormFormSet = forms.formset_factory(TatuagemForm, extra=1)
