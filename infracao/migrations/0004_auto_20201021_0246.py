# Generated by Django 2.2.12 on 2020-10-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infracao', '0003_auto_20200818_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='status',
            field=models.CharField(choices=[('foragido', 'Foragido'), ('morto', 'Morto'), ('preso', 'Preso'), ('solto', 'Livre'), ('torno', 'Tornozelado')], default='foragido', max_length=8),
        ),
    ]
