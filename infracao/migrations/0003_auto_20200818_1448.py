# Generated by Django 2.2.13 on 2020-08-18 17:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('infracao', '0002_auto_20200728_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('operacao', models.CharField(help_text='Número da Operação', max_length=15)),
                ('descricao', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'operacao',
                'verbose_name_plural': 'operacoes',
                'ordering': ('operacao',),
            },
        ),
        migrations.AddField(
            model_name='infracao',
            name='operacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operacoes', to='infracao.Operacao', verbose_name='operacao'),
        ),
    ]
