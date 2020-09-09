# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-09 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('nombre', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrafanaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_admin', models.CharField(blank=True, max_length=100)),
                ('token_viewer', models.CharField(blank=True, max_length=100)),
                ('id_org', models.IntegerField(null=True)),
                ('uuid_dashboard', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrafanaDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_db', models.UUIDField()),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_dashboard', to='graficas.Empresa')),
            ],
        ),
    ]