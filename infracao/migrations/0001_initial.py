# Generated by Django 2.2.12 on 2020-07-11 03:30

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('arma', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'arma',
                'verbose_name_plural': 'armas',
                'ordering': ('arma',),
            },
        ),
        migrations.CreateModel(
            name='Natureza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('artigo', models.CharField(help_text='Número do artigo', max_length=15)),
                ('natureza', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'natureza',
                'verbose_name_plural': 'naturezas',
                'ordering': ('natureza',),
            },
        ),
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('qualificacao', models.CharField(choices=[('aut', 'Autor'), ('coaut', 'Co-Autor'), ('part', 'Participe'), ('vit', 'Vitima')], default='aut', max_length=5, verbose_name='qualificação')),
                ('status', models.CharField(choices=[('foragido', 'Foragido'), ('morto', 'Morto'), ('preso', 'Preso'), ('solto', 'Solto')], default='foragido', max_length=8)),
                ('arma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armas', to='infracao.Arma', verbose_name='arma de fogo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('natureza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='naturezas', to='infracao.Natureza', verbose_name='natureza')),
                ('pessoa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='pessoa.Pessoa')),
            ],
            options={
                'verbose_name': 'infração',
                'verbose_name_plural': 'infrações',
                'ordering': ('-created',),
            },
        ),
    ]
