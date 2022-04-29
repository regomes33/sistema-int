# Generated by Django 2.2.24 on 2022-04-28 19:08

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homicidio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diligencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('diligencia', models.CharField(max_length=300, verbose_name='diligência')),
            ],
            options={
                'verbose_name': 'diligência',
                'verbose_name_plural': 'diligências',
                'ordering': ('diligencia',),
            },
        ),
        migrations.AddField(
            model_name='autoria',
            name='nomeAutor',
            field=models.CharField(default=1, max_length=50, verbose_name='nome autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autoria',
            name='sobrenomeAutor',
            field=models.CharField(default=1, max_length=50, verbose_name='sobre nome autor'),
            preserve_default=False,
        ),
    ]
