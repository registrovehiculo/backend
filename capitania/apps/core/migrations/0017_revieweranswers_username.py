# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2021-05-31 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_revieweranswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='revieweranswers',
            name='username',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]