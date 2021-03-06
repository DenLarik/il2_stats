# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-14 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_sorties_streak'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerOnline',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=128)),
                ('coalition', models.IntegerField(choices=[(1, 'Allies'), (2, 'Axis')])),
                ('date', models.DateTimeField(auto_now=True, db_index=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Profile')),
            ],
            options={
                'verbose_name_plural': 'players online',
                'db_table': 'online',
                'verbose_name': 'player online',
            },
        ),
        migrations.AlterField(
            model_name='sortie',
            name='nickname',
            field=models.CharField(max_length=128),
        ),
    ]
