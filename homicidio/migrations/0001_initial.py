# Generated by Django 2.2.12 on 2020-07-11 03:30

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('infracao', '0001_initial'),
        ('ocorrencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaUpm',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('area_upm', models.CharField(max_length=50,
                                              unique=True, verbose_name='área UPM')),
            ],
            options={
                'verbose_name': 'area upm',
                'verbose_name_plural': 'area upms',
                'ordering': ('area_upm',),
            },
        ),
        migrations.CreateModel(
            name='Autoria',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('autoria', models.CharField(max_length=50, verbose_name='autoria')),
            ],
            options={
                'verbose_name': 'autoria',
                'verbose_name_plural': 'autorias',
                'ordering': ('autoria',),
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('genero', models.CharField(max_length=50, verbose_name='genero')),
            ],
            options={
                'verbose_name': 'genero',
                'verbose_name_plural': 'generos',
                'ordering': ('genero',),
            },
        ),
        migrations.CreateModel(
            name='Motivacao',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('titulo', models.CharField(max_length=50,
                                            unique=True, verbose_name='título')),
            ],
            options={
                'verbose_name': 'motivação',
                'verbose_name_plural': 'motivações',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Homicidio',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(
                    auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True,
                                             max_length=100, null=True, verbose_name='endereço')),
                ('address_number', models.IntegerField(
                    blank=True, null=True, verbose_name='número')),
                ('complement', models.CharField(blank=True,
                                                max_length=100, null=True, verbose_name='complemento')),
                ('cep', models.CharField(blank=True,
                                         max_length=9, null=True, verbose_name='CEP')),
                ('country', models.CharField(blank=True, default='Brasil',
                                             max_length=50, null=True, verbose_name='país')),
                ('data_do_homicidio', models.DateField(
                    verbose_name='Data do Homicídio')),
                ('forma', models.CharField(choices=[
                 ('tentado', 'Tentado'), ('consumado', 'Consumado')], default='tentado', max_length=10)),
                ('area_upm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               to='homicidio.AreaUpm', verbose_name='área UPM')),
                ('autoria', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.CASCADE, to='homicidio.Autoria', verbose_name='Autoria')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                 to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('district', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.SET_NULL, to='core.District', verbose_name='bairro')),
                ('genero', models.ForeignKey(blank=True, null=True,
                                             on_delete=django.db.models.deletion.CASCADE, to='homicidio.Genero', verbose_name='Genero')),
                ('instrumento', models.ForeignKey(blank=True, null=True,
                                                  on_delete=django.db.models.deletion.SET_NULL, to='infracao.Arma')),
                ('motivacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                to='homicidio.Motivacao', verbose_name='motivação')),
                ('rai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                          to='ocorrencia.Ocorrencia', verbose_name='rai da Ocorrência')),
                ('vitima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             to='pessoa.Pessoa', verbose_name='vítima')),
            ],
            options={
                'verbose_name': 'homicídio',
                'verbose_name_plural': 'homicídios',
                'ordering': ('-data_do_homicidio',),
            },
        ),
    ]
