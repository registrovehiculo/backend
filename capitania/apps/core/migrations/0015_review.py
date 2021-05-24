# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2021-05-24 12:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210510_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(null=True)),
                ('text', models.CharField(max_length=200)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
                'db_table': 'review',
            },
        ),
    ]
