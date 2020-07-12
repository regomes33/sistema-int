from django.db import models
from core.models import UuidModel, TimeStampedModel, CreatedBy, Address
from ocorrencia.models import Ocorrencia
from pessoa.models import Pessoa
from infracao.models import Arma
from utils.data import FORMA


class AreaUpm(UuidModel, models.Model):
    area_upm = models.CharField('área UPM', max_length=50, unique=True)

    class Meta:
        ordering = ('area_upm',)
        verbose_name = 'area upm'
        verbose_name_plural = 'area upms'

    def __str__(self):
        return self.area_upm


class Autoria(UuidModel, models.Model):
    autoria = models.CharField('autoria', max_length=50)

    class Meta:
        ordering = ('autoria',)
        verbose_name = 'autoria'
        verbose_name_plural = 'autorias'

    def __str__(self):
        return self.autoria


class Genero(UuidModel, models.Model):
    genero = models.CharField('genero', max_length=50)

    class Meta:
        ordering = ('genero',)
        verbose_name = 'genero'
        verbose_name_plural = 'generos'

    def __str__(self):
        return self.genero


class Motivacao(UuidModel, models.Model):
    titulo = models.CharField('título', max_length=50, unique=True)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'motivação'
        verbose_name_plural = 'motivações'

    def __str__(self):
        return self.titulo


class Homicidio(UuidModel, Address, CreatedBy, TimeStampedModel):
    rai = models.ForeignKey(
        Ocorrencia,
        verbose_name='rai da Ocorrência',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data_do_homicidio = models.DateField('Data do Homicídio')
    forma = models.CharField(max_length=10, choices=FORMA, default='tentado')
    area_upm = models.ForeignKey(
        AreaUpm,
        verbose_name='área UPM',
        on_delete=models.CASCADE
    )
    autoria = models.ForeignKey(
        Autoria,
        verbose_name='Autoria',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    genero = models.ForeignKey(
        Genero,
        verbose_name='Genero',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    vitima = models.ForeignKey(
        Pessoa,
        verbose_name='vítima',
        on_delete=models.CASCADE,
    )
    instrumento = models.ForeignKey(
        Arma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    motivacao = models.ForeignKey(
        Motivacao,
        verbose_name='motivação',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-data_do_homicidio',)
        verbose_name = 'homicídio'
        verbose_name_plural = 'homicídios'

    def __str__(self):
        return str(self.rai)

    # def get_absolute_url(self):
    #     return reverse_lazy('ocorrencia:homicidios')
