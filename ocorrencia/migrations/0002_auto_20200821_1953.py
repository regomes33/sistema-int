# Generated by Django 2.2.12 on 2020-08-21 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ocorrencia',
            options={'ordering': ('-data_do_fato',), 'verbose_name': 'ocorrência', 'verbose_name_plural': 'ocorrências'},
        ),
    ]
