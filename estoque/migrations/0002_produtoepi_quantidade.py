# Generated by Django 4.2.4 on 2023-09-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoepi',
            name='Quantidade',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade em Estoque'),
        ),
    ]
