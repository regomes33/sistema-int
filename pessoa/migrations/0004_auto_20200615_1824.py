# Generated by Django 2.2.12 on 2020-06-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(blank=True, help_text='Data no formato dd/mm/YYYY', null=True, verbose_name='data de nascimento'),
        ),
    ]
