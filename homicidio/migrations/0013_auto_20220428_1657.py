# Generated by Django 2.2.24 on 2022-04-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homicidio', '0012_auto_20220428_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homicidio',
            name='diligencia',
            field=models.TextField(
                blank=True, max_length=5000, null=True, verbose_name='diligências'),
        ),
    ]
