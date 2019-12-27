from django.db import models


# Create your models here.
class Veiculo(models.Model):

    placa = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    cor = models.CharField(max_length=100, null=True, blank=True)
