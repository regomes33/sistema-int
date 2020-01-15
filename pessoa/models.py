''' FINALIZAR E OTIMIZAR '''
# from pip._internal.utils.outdated import SELFCHECK_DATE_FMT
import re

from django.core import validators
from django.db.models import FileField
from localflavor.br.br_states import STATE_CHOICES

''' FALTA TATUAGEM, COMPARSAS '''
''' Models responsável pelo gerenciamento de pessoa '''
''' Módel é único de pessoa '''
from django.db import models

# Create your models here.
''' model com informações básicas de pessoa '''


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=50, null=True, blank=True)
    sobrenome = models.CharField('sobrenome', max_length=100,
                                 null=True, blank=True, )
    apelido = models.CharField(max_length=50,
                               null=True, blank=True)
    mae = models.CharField(max_length=50,
                           null=True, blank=True)
    pai = models.CharField(max_length=50,
                           null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True, )

    def __str__(self):
        return self.nome + ' ' + self.sobrenome + ' '+'CPF: '+self.cpf

    def clean_name(self):
        return self.cleaned_data["nome"].upper()
    def clean_cpf(self):
        return self.cleaned_data["cpf"].upper()
    def clean_sobrenome(self):
        return self.cleaned_data["sobrenome"].upper()

    #
    # @property
    # def getNomeCompleto(self):
    #     return self.nome + ' ' + self.sobrenome

    class META:
        ordering = 'nome'
        verbose_name = 'nome'
        verbose_name_plural = 'nomes'


class PessoaFoto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fotopessoa = models.ImageField('Imagem da Pessoa', upload_to="pessoa")


''' model com informações de documento da pessoa '''

# class META:
#     ordering = 'cpf'
#     verbose_name = 'cpf'
#     verbose_name_plural: 'cpfs'


''' model com informações de contato da pessoa '''


class PessoaContato(models.Model):
    CONTATOS = {
        ('cel', 'Celular'),
        ('tel', 'Telefone'),
    }

    pessoa = models.ForeignKey(Pessoa,
                               on_delete=models.CASCADE)
    categoria = models.CharField(max_length=10,
                                 choices=CONTATOS)
    contato = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.categoria + ': ' + self.contato


''' model com informações de endereço da pessoa '''


class PessoaEndereco(models.Model):
    pessoa = models.ForeignKey(Pessoa,
                               on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200,
                                   null=True, blank=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField('UF', max_length=100, choices=STATE_CHOICES)
    pais = models.CharField(max_length=50,
                            default='Brasil')

    # def __str__(self):
    #     return self.endereco + ', ' + self.cidade + ', ' + self.estado + ', ' + self.pais


class Comparsas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    comparsas = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.comparsas


class Tatuagem(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fototatuagem = models.ImageField('Imagem da Tatuagem', upload_to="tatuagem")
    descricaotatuagem = models.TextField('Descrição da Tatuagem', max_length=500, null=True, blank=True)
