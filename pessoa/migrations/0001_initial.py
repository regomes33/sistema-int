# Generated by Django 2.2.5 on 2020-01-24 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='nome')),
                ('sobrenome', models.CharField(blank=True, max_length=100, null=True, verbose_name='sobrenome')),
                ('apelido', models.CharField(blank=True, max_length=50, null=True)),
                ('mae', models.CharField(blank=True, max_length=50, null=True)),
                ('pai', models.CharField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tatuagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fototatuagem', models.ImageField(upload_to='tatuagem', verbose_name='Imagem da Tatuagem')),
                ('descricaotatuagem', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição da Tatuagem')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotopessoa', models.ImageField(upload_to='pessoa', verbose_name='Imagem da Pessoa')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=100, verbose_name='UF')),
                ('pais', models.CharField(default='Brasil', max_length=50)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('cel', 'Celular'), ('tel', 'Telefone')], max_length=10)),
                ('contato', models.CharField(max_length=30)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Comparsas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparsas', models.CharField(blank=True, max_length=100, null=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
    ]
