# Generated by Django 4.0.3 on 2022-04-10 21:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tempo', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField(blank=True, verbose_name=datetime.datetime(2022, 4, 10, 21, 6, 49, 539590))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Barbeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField(blank=True, verbose_name=datetime.datetime(2022, 4, 10, 21, 6, 49, 539043))),
                ('foto', models.ImageField(blank=True, upload_to='fotos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
