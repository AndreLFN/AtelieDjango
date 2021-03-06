# Generated by Django 3.1.5 on 2021-01-15 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.FloatField()),
                ('imagem', models.FilePathField(path='/img')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_da_venda', models.TimeField()),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_de_vendas.registro')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(max_length=30)),
                ('quantidade', models.IntegerField()),
                ('valor_venda', models.FloatField()),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_de_vendas.venda')),
            ],
        ),
    ]
