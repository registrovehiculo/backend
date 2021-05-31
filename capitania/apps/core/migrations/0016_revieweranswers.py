# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2021-05-27 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewerAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(null=True)),
                ('text', models.CharField(max_length=200)),
                ('reviewer_answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer_answers', to='core.Review', verbose_name='Review')),
            ],
            options={
                'verbose_name': 'respuestas',
                'verbose_name_plural': 'respuestas',
                'db_table': 'ReviewerAnswers',
            },
        ),
    ]