# Generated by Django 2.2.10 on 2020-03-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0009_auto_20200307_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='natureza',
            name='artigo',
            field=models.CharField(default=1, help_text='Número do artigo', max_length=15),
            preserve_default=False,
        ),
    ]