# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20160321_1741'),
        ('stats', '0015_player_squad'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='squads.Squad'),
        ),
        migrations.AlterField(
            model_name='player',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='stats.Profile'),
        ),
    ]
