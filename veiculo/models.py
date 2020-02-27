from django.db import models
from django.urls import reverse_lazy
from core.models import TimeStampedModel


class Veiculo(TimeStampedModel):
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

    class Meta:
        ordering = ('placa',)
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return f'{self.placa} - {self.modelo} - {self.cor}'

    def get_absolute_url(self):
        return reverse_lazy('veiculo:veiculos')

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.__str__(),
        }


class Modelo(models.Model):
    modelo = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ('modelo',)
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse_lazy('veiculo:modelos')


class Cor(models.Model):
    cor = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('cor',)
        verbose_name = 'cor'
        verbose_name_plural = 'cores'

    def __str__(self):
        return self.cor
