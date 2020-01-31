from django.db import models
from core.models import TimeStampedModel, CreatedBy, Address, Document


class Pessoa(TimeStampedModel, CreatedBy, Address, Document):
    nome = models.CharField('nome', max_length=50, null=True, blank=True)
    sobrenome = models.CharField(
        'sobrenome',
        max_length=100,
        null=True,
        blank=True,
    )
    apelido = models.CharField(max_length=50, null=True, blank=True)
    mae = models.CharField(max_length=50, null=True, blank=True)
    pai = models.CharField(max_length=50, null=True, blank=True)
    faccao = models.ForeignKey(
        'Faccao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class META:
        ordering = ('nome',)
        verbose_name = 'nome'
        verbose_name_plural = 'nomes'

    def __str__(self):
        return ' '.join(filter(None, [self.nome, self.sobrenome]))


class PessoaFoto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fotopessoa = models.ImageField('Imagem da Pessoa', upload_to="pessoa")


class PessoaContato(models.Model):
    '''
    Telefones
    '''
    CONTATOS = (
        ('cel', 'Celular'),
        ('tel', 'Telefone'),
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    categoria = models.CharField(
        max_length=10,
        choices=CONTATOS,
        default='cel'
    )
    contato = models.CharField(max_length=50)


class Comparsa(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_comparsa = models.CharField(
        'nome',
        max_length=100,
        null=True,
        blank=True
    )


class Tatuagem(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    foto_tatuagem = models.ImageField(
        'Imagem da Tatuagem',
        upload_to="tatuagem"
    )
    descricao = models.TextField(
        'Descrição da Tatuagem',
        null=True,
        blank=True
    )


class Infracao(models.Model):
    '''
    Natureza
    '''
    NATUREZA = [
        ('art.28', 'Art. 28. Usuário'),
        ('art.33', 'Art. 33. Trafico de Drogas'),
        ('Art.34', 'Art. 34. Maquinario'),
        ('Art.35', 'Art. 35. Associarem-se duas ou mais pessoas para o Trafico'),
        ('Art.36', 'Art. 36. Financiar Financiamento do Trafico'),
        ('Art.121', 'Art.121. Matar Alguem'),
        ('art.155', 'Art. 155. Furto'),
        ('art.157', 'Art. 157. Roubo'),
        ('art.157§3º', 'Art 157. §3º - Roubo Com Lesão Corporal'),
        ('art.157§3º', 'Art 157. §3º -   Roubo Seguido de Morte (Latrocinio)'),
        ('art.171', '  Art. 171. Estelionato'),
        ('Lei.12850', 'Lei : 12850. Associação Criminosa')
    ]

    QUALIFICACAO = (
        ('aut', 'Autor'),
        ('coaut', 'Co-Autor'),
        ('part', 'Participe'),
        ('vit', 'Vitima')
    )

    ARMA_DE_FOGO = (
        ('revolver', 'Revolver'),
        ('pistola', 'Pistola'),
        ('faca', 'Faca')
    )
    STATUS = (
        ('vivo', 'Vivo'),
        ('morto', 'Morto'),
        ('preso', 'Preso'),
        ('solto', 'Solto')
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    primeiranatureza = models.CharField(
        'Primeira Natureza',
        max_length=50,
        choices=NATUREZA,
        null=True,
        blank=True,
    )
    qualificacao = models.CharField(
        max_length=5,
        choices=QUALIFICACAO,
        default='aut',
    )
    segundanatureza = models.CharField(
        'Segunda Natureza',
        max_length=50,
        choices=NATUREZA,
        null=True,
        blank=True,
    )
    arma_de_fogo = models.CharField(
        max_length=10,
        choices=ARMA_DE_FOGO,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=5,
        choices=STATUS,
        default='vivo'
    )


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


class Ocorrencia(models.Model):
    rai = models.CharField(max_length=100, null=True, blank=True)
    data_do_fato = models.DateField('Data do Fato')
    descricao = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ('rai',)
        verbose_name = 'ocorrencia'
        verbose_name_plural = 'ocorrencias'

    def __str__(self):
        return self.rai


class PessoaOcorrencia(TimeStampedModel):
    pessoa = models.ForeignKey(
        Pessoa,
        related_name='pessoas',
        on_delete=models.CASCADE,
    )
    ocorrencia = models.ForeignKey(
        Ocorrencia,
        related_name='ocorrencias',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.ocorrencia}'


class Veiculo(models.Model):
    placa = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    cor = models.CharField(max_length=100, null=True, blank=True)
