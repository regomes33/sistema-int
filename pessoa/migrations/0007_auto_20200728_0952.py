# Generated by Django 2.2.12 on 2020-07-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_pessoa_observacao_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='status_atual',
            field=models.CharField(choices=[('foragido', 'Foragido'), ('morto', 'Morto'), ('preso', 'Preso'), ('solto', 'Livre')], default='foragido', max_length=8),
        ),
    ]
