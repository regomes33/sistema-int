# Generated by Django 2.2.24 on 2022-04-28 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homicidio', '0004_auto_20220428_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homicidio',
            name='autor',
        ),
        migrations.AddField(
            model_name='homicidio',
            name='nomeautor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='homicidio.Autor', verbose_name='Nome Autor'),
        ),
    ]
