# Generated by Django 2.2.24 on 2023-01-10 19:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('cor', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'cor',
                'verbose_name_plural': 'cores',
                'ordering': ('cor',),
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('modelo', models.CharField(max_length=70, unique=True)),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
                'ordering': ('modelo',),
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('placa', models.CharField(blank=True, max_length=100, null=True)),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cores', to='veiculo.Cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelos', to='veiculo.Modelo')),
            ],
            options={
                'verbose_name': 'veículo',
                'verbose_name_plural': 'veículos',
                'ordering': ('placa',),
            },
        ),
    ]
