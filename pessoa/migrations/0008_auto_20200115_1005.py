# Generated by Django 2.2.5 on 2020-01-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_auto_20191213_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoacontato',
            name='categoria',
            field=models.CharField(choices=[('cel', 'Celular'), ('tel', 'Telefone')], max_length=10),
        ),
    ]
