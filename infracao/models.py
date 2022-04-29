from django.db import models
from django.urls import reverse_lazy

from core.models import CreatedBy, TimeStampedModel, UuidModel
from pessoa.models import Pessoa
from utils.data import QUALIFICACAO, STATUS


class Arma(UuidModel):
    arma = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('arma',)
        verbose_name = 'arma'
        verbose_name_plural = 'armas'

    def __str__(self):
        return self.arma

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.arma,
        }


class Natureza(UuidModel):
    artigo = models.CharField(max_length=15, help_text='Número do artigo')
    natureza = models.TextField(unique=True)

    class Meta:
        ordering = ('natureza',)
        verbose_name = 'natureza'
        verbose_name_plural = 'naturezas'

    def __str__(self):
        return self.natureza

    def get_absolute_url(self):
        return reverse_lazy('infracao:natureza_list')

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.natureza,
        }


class Operacao(UuidModel):
    operacao = models.CharField(max_length=15, help_text='Número da Operação')
    descricao = models.TextField(unique=True)

    class Meta:
        ordering = ('operacao',)
        verbose_name = 'operacao'
        verbose_name_plural = 'operacoes'

    def __str__(self):
        return self.operacao + ' - ' + self.descricao

    def get_absolute_url(self):
        return reverse_lazy('infracao:operacao_list')

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.operacao + ' - ' + self.descricao
        }


class Infracao(UuidModel, CreatedBy, TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True)
    natureza = models.ForeignKey(
        Natureza,
        on_delete=models.SET_NULL,
        verbose_name='natureza',
        related_name='naturezas',
        null=True,
        blank=True
    )
    operacao = models.ForeignKey(
        Operacao,
        on_delete=models.SET_NULL,
        verbose_name='operacao',
        related_name='operacoes',
        null=True,
        blank=True
    )
    qualificacao = models.CharField(
        'qualificação',
        max_length=5,
        choices=QUALIFICACAO,
        default='aut',
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
        max_length=8,
        choices=STATUS,
        default='foragido'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'infração'
        verbose_name_plural = 'infrações'

    def __str__(self):
        return f'{self.pessoa} - {self.natureza} -{self.operacao}'

    def get_absolute_url(self):
        return reverse_lazy('infracao:infracao_list')
