# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-16 19:32
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0031_vlifes_step_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='is_hide',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
