# Generated by Django 4.2.4 on 2023-09-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_produto_possuica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='AprovadoPara',
            new_name='aprovadoPara',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='CA',
            new_name='ca',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='DataDeValidade',
            new_name='dataDeValidade',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Equipamento',
            new_name='equipamento',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Marcacao',
            new_name='marcacao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Natureza',
            new_name='natureza',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Observacao',
            new_name='observacao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='PossuiCA',
            new_name='possuiCA',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Quantidade',
            new_name='quantidade',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='Situacao',
            new_name='situacao',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='Cor',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='DescricaoEquipamento',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='RazaoSocial',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='Referencia',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='Restricao',
        ),
        migrations.AddField(
            model_name='produto',
            name='nDoLaudo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='nProcesso',
            field=models.CharField(max_length=50, null=True),
        ),
    ]