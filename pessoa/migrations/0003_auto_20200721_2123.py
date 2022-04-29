# Generated by Django 2.2.12 on 2020-07-22 00:23

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_pessoa_status_atual'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comparsa',
            options={'ordering': (
                'nome',), 'verbose_name': 'comparsa', 'verbose_name_plural': 'comparsas'},
        ),
        migrations.RemoveField(
            model_name='comparsa',
            name='grau_parentesco',
        ),
        migrations.RemoveField(
            model_name='comparsa',
            name='observacao',
        ),
        migrations.RemoveField(
            model_name='comparsa',
            name='parente',
        ),
        migrations.RemoveField(
            model_name='comparsa',
            name='pessoa',
        ),
        migrations.AlterField(
            model_name='comparsa',
            name='nome',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PessoaComparsa',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(
                    default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(
                    auto_now=True, verbose_name='modificado em')),
                ('parente', models.BooleanField(default=False)),
                ('grau_parentesco', models.CharField(
                    blank=True, max_length=50, null=True)),
                ('observacao', models.TextField(
                    blank=True, max_length=500, null=True)),
                ('comparsa', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.SET_NULL, related_name='comparsas', to='pessoa.Comparsa')),
                ('pessoa', models.ForeignKey(
                    blank=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
            options={
                'ordering': ('pessoa', 'comparsa'),
            },
        ),
    ]
