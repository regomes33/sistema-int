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

    class Meta:
        ordering = ('nome',)
        verbose_name = 'nome'
        verbose_name_plural = 'nomes'

    def __str__(self):
        return ' '.join(filter(None, [self.nome, self.sobrenome]))


class PessoaFoto(TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fotopessoa = models.ImageField('Imagem da Pessoa', upload_to="pessoa")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class PessoaContato(TimeStampedModel):
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

    class Meta:
        ordering = ('pessoa', 'contato')
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.contato


class Comparsa(TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_comparsa = models.CharField(
        'nome',
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('pessoa', 'nome_comparsa')
        verbose_name = 'comparsa'
        verbose_name_plural = 'comparsas'

    def __str__(self):
        return self.nome_comparsa


class Tatuagem(TimeStampedModel):
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

    class Meta:
        ordering = ('pessoa', '-created')
        verbose_name = 'tatuagem'
        verbose_name_plural = 'tatuagens'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class Natureza(models.Model):
    natureza = models.TextField(unique=True)

    class Meta:
        ordering = ('natureza',)
        verbose_name = 'natureza'
        verbose_name_plural = 'naturezas'

    def __str__(self):
        return self.natureza


class Arma(models.Model):
    arma = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('arma',)
        verbose_name = 'arma'
        verbose_name_plural = 'armas'

    def __str__(self):
        return self.arma


class Infracao(TimeStampedModel):
    QUALIFICACAO = (
        ('aut', 'Autor'),
        ('coaut', 'Co-Autor'),
        ('part', 'Participe'),
        ('vit', 'Vitima')
    )
    STATUS = (
        ('vivo', 'Vivo'),
        ('morto', 'Morto'),
        ('preso', 'Preso'),
        ('solto', 'Solto')
    )
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    primeira_natureza = models.ForeignKey(
        Natureza,
        on_delete=models.SET_NULL,
        verbose_name='primeira natureza',
        related_name='natureza1',
        null=True,
        blank=True
    )
    qualificacao = models.CharField(
        max_length=5,
        choices=QUALIFICACAO,
        default='aut',
    )
    segunda_natureza = models.ForeignKey(
        Natureza,
        on_delete=models.SET_NULL,
        verbose_name='segunda natureza',
        related_name='natureza2',
        null=True,
        blank=True
    )
    arma = models.ForeignKey(
        Arma,
        on_delete=models.SET_NULL,
        verbose_name='arma de fogo',
        related_name='armas',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=5,
        choices=STATUS,
        default='vivo'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'infração'
        verbose_name_plural = 'infrações'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class Faccao(models.Model):
    FUNCAO_CHOICES = (
        ('chefe', 'Chefe'),
        ('membro', 'Membro'),
    )
    nome = models.CharField(max_length=100, unique=True)
    funcao = models.CharField(
        max_length=10,
        choices=FUNCAO_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'facção'
        verbose_name_plural = 'facções'

    def __str__(self):
        return self.nome


class Ocorrencia(TimeStampedModel):
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
    '''
    Uma pessoa pode ter várias ocorrências.
    '''
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


class Veiculo(TimeStampedModel):
    placa = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.ForeignKey(
        'Modelo',
        on_delete=models.PROTECT,
        related_name='modelos',
    )
    cor = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('placa',)
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return f'{self.placa} - {self.modelo} - {self.cor}'


class Modelo(models.Model):
    modelo = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ('modelo',)
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return self.modelo
