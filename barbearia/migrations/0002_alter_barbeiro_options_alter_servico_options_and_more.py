# Generated by Django 4.0.3 on 2022-04-10 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barbeiro',
            options={'ordering': ['nome'], 'verbose_name': 'Barbeiro', 'verbose_name_plural': 'Barbeiros'},
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ['nome'], 'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nome'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='barbeiro',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2022, 4, 10, 22, 43, 46, 154801)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2022, 4, 10, 22, 43, 46, 155556)),
        ),
    ]
