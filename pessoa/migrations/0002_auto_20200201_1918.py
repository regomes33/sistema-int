# Generated by Django 2.2.5 on 2020-02-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comparsa',
            options={'ordering': ('pessoa', 'nome'), 'verbose_name': 'comparsa', 'verbose_name_plural': 'comparsas'},
        ),
        migrations.RemoveField(
            model_name='comparsa',
            name='nome_comparsa',
        ),
        migrations.AddField(
            model_name='comparsa',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
