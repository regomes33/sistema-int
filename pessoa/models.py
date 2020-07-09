from django.db import models
from core.models import UuidModel, TimeStampedModel, CreatedBy, Address, Document
from veiculo.models import Veiculo
from utils.data import TIPO


class Pessoa(UuidModel, TimeStampedModel, CreatedBy, Address, Document):
    nome = models.CharField('nome', max_length=50)
    sobrenome = models.CharField('sobrenome', max_length=100)
    apelido = models.CharField(max_length=50, null=True, blank=True)
    mae = models.CharField('mãe', max_length=50, null=True, blank=True)
    pai = models.CharField(max_length=50, null=True, blank=True)
    observacao = models.TextField(
        'Observação', max_length=500, null=True, blank=True)
    faccao = models.ForeignKey(
        'Faccao',
        on_delete=models.SET_NULL,
        verbose_name='facção',
        null=True,
        blank=True
    )
    vitima = models.BooleanField(default=False)
    nascimento = models.DateField(
        'data de nascimento',
        null=True,
        blank=True,
        help_text='Data no formato dd/mm/YYYY'
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return ' '.join(filter(None, [self.nome, self.sobrenome]))

    def get_address(self):
        if self.address:
            return f'{self.address}, {self.address_number or ""} {self.complement or ""}'

    def get_address_complement(self):
        # return ' - '.join(filter(None, [self.district, self.district.city,
        # self.uf]))
        return 'address_complement'

    def get_first_photo(self):
        '''
        Retorna somente a primeira foto.
        '''
        photos = self.foto_set.all()
        if photos:
            return photos[0]

    def to_dict(self):
        # document_dict = Document.to_dict_base(self)
        # address_dict = Address.to_dict_base(self)
        return {
            'pk': self.pk,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'apelido': self.apelido,
            'mae': self.mae,
            'pai': self.pai,
            'nascimento': self.nascimento,
            # **document_dict,
            # **address_dict,
            # 'full_address': self.get_address(),
            # 'address_complement': self.get_address_complement(),
            # 'cep': self.cep,
        }


class Foto(UuidModel, TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True)
    foto = models.ImageField('Imagem da Pessoa', upload_to="pessoa")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class Tatuagem(UuidModel, TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True)
    foto = models.ImageField('Imagem da Tatuagem', upload_to="tatuagem")
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


class PessoaContato(UuidModel, TimeStampedModel):
    '''
    Telefones
    '''
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)
    tipo = models.CharField(
        max_length=10,
        choices=TIPO,
        default='cel'
    )
    telefone = models.CharField(max_length=20)

    class Meta:
        ordering = ('pessoa', 'telefone')
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return f'{self.pessoa} - {self.telefone}'


class Comparsa(UuidModel, TimeStampedModel, Document):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)
    nome = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    parente = models.BooleanField(default=False)
    grau_parentesco = models.CharField(max_length=50, null=True, blank=True)
    observacao = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ('pessoa', 'nome')
        verbose_name = 'comparsa'
        verbose_name_plural = 'comparsas'

    def __str__(self):
        if self.nome:
            return self.nome
        return str(self.pk)


class Faccao(UuidModel):
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

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.nome,
        }


class PessoaVeiculo(UuidModel, CreatedBy, TimeStampedModel):
    '''
    Uma pessoa pode ter vários veículos.
    '''
    pessoa = models.ForeignKey(
        'Pessoa',
        related_name='pessoas_veiculos',
        on_delete=models.CASCADE,
        blank=True
    )
    veiculo = models.ForeignKey(
        Veiculo,
        related_name='veiculos2',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.veiculo}'

    def get_veiculo(self):
        return self.veiculo
