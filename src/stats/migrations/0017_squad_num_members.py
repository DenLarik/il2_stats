# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0016_auto_20160404_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='num_members',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
