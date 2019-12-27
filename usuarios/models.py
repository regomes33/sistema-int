from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='usuario')
    rgfuncional = models.CharField(max_length=5, help_text='00000')
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
