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
