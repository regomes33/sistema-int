# Generated by Django 2.2.12 on 2020-10-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0002_auto_20200821_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='rai',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='RAI'),
        ),
    ]
