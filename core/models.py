import uuid
from django.contrib.auth.models import User
from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class UuidModel(models.Model):
    slug = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class City(models.Model):
    name = models.CharField('cidade', max_length=100)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'


class District(models.Model):
    name = models.CharField('bairro', max_length=100)
    city = models.ForeignKey(
        'City',
        verbose_name='cidade',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'bairro'
        verbose_name_plural = 'bairros'

    def to_dict(self):
        return {
            'value': self.pk,
            'text': f'{self.name} - {self.city}',
        }


class Address(models.Model):
    address = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    address_number = models.IntegerField('número', null=True, blank=True)
    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        District,
        verbose_name='bairro',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)
    country = models.CharField(
        'país',
        max_length=50,
        default='Brasil',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'address': self.address,
            'address_number': self.address_number,
            'complement': self.complement,
            'district': self.district,
            'city': self.city,
            'uf': self.uf,
            'cep': self.cep,
        }


class Document(models.Model):
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField('RG', max_length=11, null=True, blank=True)
    cnh = models.CharField('CNH', max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'cpf': self.cpf,
            'rg': self.rg,
            'cnh': self.cnh,
        }


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)
    exist_deleted = models.BooleanField(
        'existe/deletado',
        default=True,
        help_text='Se for True o item existe. Se for False o item foi deletado.'
    )

    class Meta:
        abstract = True
