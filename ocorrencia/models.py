from django.db import models
from django.urls import reverse_lazy
from core.models import UuidModel, TimeStampedModel, CreatedBy, Address
from pessoa.models import Pessoa, Veiculo
from infracao.models import Arma, Natureza, Infracao


class Ocorrencia(UuidModel, CreatedBy, TimeStampedModel):
    rai = models.IntegerField('RAI', null=True, blank=True)
    data_do_fato = models.DateField('Data do Fato')
    descricao = models.TextField('descrição', null=True, blank=True)

    class Meta:
        ordering = ('rai',)
        verbose_name = 'ocorrência'
        verbose_name_plural = 'ocorrências'

    def __str__(self):
        return str(self.rai)

    # def get_absolute_url(self):
    # return reverse_lazy('ocorrencia:ocorrencia', kwargs={'slug': self.slug})

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.rai,
        }


class PessoaOcorrencia(UuidModel, CreatedBy, TimeStampedModel):
    '''
    Uma pessoa pode ter várias ocorrências.
    '''
    pessoa = models.ForeignKey(
        Pessoa,
        related_name='pessoas_ocorrencias',
        on_delete=models.CASCADE,
        blank=True
    )
    ocorrencia = models.ForeignKey(
        Ocorrencia,
        related_name='ocorrencias1',
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.ocorrencia}'


class OcorrenciaVeiculo(UuidModel, CreatedBy, TimeStampedModel):
    '''
    Uma ocorrência pode ter vários veículos.
    '''
    ocorrencia = models.ForeignKey(
        'Ocorrencia',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.ocorrencia} - {self.veiculo}'
