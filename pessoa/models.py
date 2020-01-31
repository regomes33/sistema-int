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

from infracao.models import Faccao as FaccaoModel

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
    cpf = models.CharField(max_length=14, blank=False,
                           null=False, unique=True, )
    faccao = models.ForeignKey(
        FaccaoModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome + ' ' + self.sobrenome + ' ' + 'CPF: ' + self.cpf

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
    '''
    Telefones
    '''
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
    # return self.endereco + ', ' + self.cidade + ', ' + self.estado + ', ' +
    # self.pais


class Comparsas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    comparsas = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.comparsas


class Tatuagem(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fototatuagem = models.ImageField(
        'Imagem da Tatuagem', upload_to="tatuagem")
    descricaotatuagem = models.TextField(
        'Descrição da Tatuagem', max_length=500, null=True, blank=True)


''' FINALIZAR E OTIMIZAR '''
''' Models responsável pelo gerenciamento de infração '''
''' Módel é único de infração '''
from django.db import models
from pessoa.models import Pessoa

# Create your models here.
''' Model com informações básicas de uma infração '''


class Infracao(models.Model):
    '''
    Natureza
    '''
    NATUREZA = [
        ('art.28', 'Art. 28. Usuário '),
        ('art.33', 'Art. 33. Trafico de Drogas'),
        ('Art.34', 'Art. 34. Maquinario '),
        ('Art.35', 'Art. 35. Associarem-se duas ou mais pessoas '
                   'para o Trafico'),
        ('Art.36', 'Art. 36. Financiar Financiamento do Trafico:'),
        ('Art.121', 'Art.121. Matar Alguem'),
        ('art.155', 'Art. 155. Furto:'),
        ('art.157', 'Art. 157. Roubo:'),
        ('art.157§3º', 'Art 157. §3º - Roubo Com Lesão Corporal ; '),
        ('art.157§3º', 'Art 157. §3º -   Roubo Seguido de Morte (Latrocionio)  '),
        ('art.171', '  Art. 171. Estelionato:'),
        ('Lei.12850', 'Lei : 12850. Associação Criminosa ')

    ]

    QUALIFICACAO = [
        ('Aut', 'Autor'),
        ('Co-Aut', 'Co-Autor'),
        ('Part', 'Participe'),
        ('Vit', 'Vitima')
    ]

    ARMA_DE_FOGO = [('Revolver', 'Revolver'),
                    ('Pistola', 'Pistola'),
                    ('Fac', 'Faca')]
    STATUS = [('Vivo', 'Vivo'),
              ('Morto', 'Morto'),
              ('Preso', 'Preso'),
              ('Solto', 'Solto')]

    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    primeiranatureza = models.CharField('Primeira Natureza', max_length=50,
                                        choices=NATUREZA, null=True, blank=True, )
    qualificacao = models.CharField(max_length=50,
                                    choices=QUALIFICACAO, null=True, blank=True)
    segundanatureza = models.CharField('Segunda Natureza', max_length=50,
                                       choices=NATUREZA, null=True, blank=True, )
    arma_de_fogo = models.CharField(
        max_length=50, null=True, blank=True, choices=ARMA_DE_FOGO)

    status = models.CharField(
        max_length=50, blank=True, null=True, choices=STATUS)

    ''' model com informações do cometimento de crime '''


class Faccao(models.Model):
    # Faccao = {
    #     ('Nenhumas', 'Nenhuma'),
    #     ('Comando Vermelho', 'Comando Vermelho'),
    #     ('PCC', 'PCC-Primeiro Comando da Capital'),
    #     ('ADE', 'ADE')
    # }
    funcao_choices = [
        ('Chefe', 'Chefe'),
        ('Membro', 'Membro'),
    ]
    nome = models.CharField(max_length=100, unique=True)
    funcao = models.CharField(
        max_length=100,
        choices=funcao_choices,
        null=True,
        blank=True
    )

    # def __str__(self):
    #     return self.faccao + ' ' + self.funcao


class Ocorrencias(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    rai = models.CharField(max_length=100, null=True, blank=True)
    data_do_fato = models.DateField('Data do Fato')
    descricao = models.CharField(max_length=500, null=True, blank=True)


class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='usuario')
    rgfuncional = models.CharField(max_length=5, help_text='00000')
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):

    placa = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    cor = models.CharField(max_length=100, null=True, blank=True)


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
