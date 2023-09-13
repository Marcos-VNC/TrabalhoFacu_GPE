# Generated by Django 4.2.4 on 2023-09-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoEPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AprovadoPara', models.CharField(max_length=255, verbose_name='Situação/Ambiente Adequado')),
                ('CA', models.CharField(max_length=20, verbose_name='Número do CA')),
                ('Cor', models.CharField(max_length=100)),
                ('DataDeValidade', models.DateField(verbose_name='Data de Validade')),
                ('DescricaoEquipamento', models.TextField(verbose_name='Descrição do Equipamento')),
                ('Equipamento', models.CharField(max_length=255, verbose_name='Nome do Equipamento')),
                ('Marcacao', models.CharField(max_length=100, verbose_name='Onde Está Escrito o CA')),
                ('Natureza', models.CharField(max_length=100, verbose_name='Natureza (Nacional ou Importado)')),
                ('Observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('RazaoSocial', models.CharField(max_length=255, verbose_name='Razão Social da Fabricante/Importadora')),
                ('Referencia', models.CharField(max_length=100, verbose_name='Referência')),
                ('Restricao', models.TextField(verbose_name='Restrição (Onde Não Pode Ser Usado)')),
                ('Situacao', models.CharField(max_length=100, verbose_name='Situação (Aprovado ou Vencido)')),
                ('Tamanho', models.CharField(max_length=50)),
            ],
        ),
    ]
