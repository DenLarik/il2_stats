# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-10-23 19:16
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0032_hide_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='order',
            field=models.CharField(db_index=True, default='', max_length=8, verbose_name='order field'),
        ),
    ]
