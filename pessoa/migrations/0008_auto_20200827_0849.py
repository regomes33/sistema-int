# Generated by Django 2.2.12 on 2020-08-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_auto_20200728_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='cidade'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='uf',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='UF'),
        ),
    ]
