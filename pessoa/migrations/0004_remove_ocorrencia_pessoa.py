# Generated by Django 2.2.5 on 2020-01-31 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoaocorrencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='pessoa',
        ),
    ]
