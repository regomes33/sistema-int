from django.db import models
from django.urls import reverse_lazy

from core.models import TimeStampedModel, UuidModel


class Veiculo(UuidModel, TimeStampedModel):
    placa = models.CharField(max_length=100, null=True, blank=True)

    modelo = models.ForeignKey(
        'Modelo',
        on_delete=models.PROTECT,
        related_name='modelos',
    )
    cor = models.ForeignKey(
        'Cor',
        on_delete=models.PROTECT,
        related_name='cores',
    )
    observacao = models.TextField(
        'Observação',
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('placa',)
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return f'{self.placa} - {self.modelo} - {self.cor}'

    def get_absolute_url(self):
        return reverse_lazy('veiculo:veiculo_list')

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.__str__(),
            'observacao': self.observacao,
        }


class Modelo(UuidModel):
    modelo = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ('modelo',)
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse_lazy('veiculo:modelo_list')


class Cor(UuidModel):
    cor = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('cor',)
        verbose_name = 'cor'
        verbose_name_plural = 'cores'

    def __str__(self):
        return self.cor
