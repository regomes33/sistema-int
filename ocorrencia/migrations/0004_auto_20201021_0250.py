# Generated by Django 2.2.12 on 2020-10-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0003_auto_20201021_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='rai',
            field=models.IntegerField(default=1, unique=True, verbose_name='RAI'),
            preserve_default=False,
        ),
    ]