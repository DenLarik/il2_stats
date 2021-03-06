# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:23
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import stats.models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0028_new_pilot_params_step_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='VLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_first_sortie', models.DateTimeField(null=True)),
                ('date_last_sortie', models.DateTimeField(null=True)),
                ('date_last_combat', models.DateTimeField(null=True)),
                ('score', models.IntegerField(db_index=True, default=0)),
                ('ratio', models.FloatField(default=1)),
                ('sorties_total', models.IntegerField(default=0)),
                ('sorties_coal', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=stats.models.default_coal_list, size=None)),
                ('sorties_cls', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_sorties_cls)),
                ('coal_pref', models.IntegerField(choices=[(0, 'neutral'), (1, 'Allies'), (2, 'Axis')], default=0)),
                ('flight_time', models.BigIntegerField(db_index=True, default=0)),
                ('ammo', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_ammo)),
                ('accuracy', models.FloatField(db_index=True, default=0)),
                ('bailout', models.IntegerField(default=0)),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
                ('captured', models.IntegerField(default=0)),
                ('relive', models.IntegerField(default=0)),
                ('takeoff', models.IntegerField(default=0)),
                ('landed', models.IntegerField(default=0)),
                ('ditched', models.IntegerField(default=0)),
                ('crashed', models.IntegerField(default=0)),
                ('in_flight', models.IntegerField(default=0)),
                ('shotdown', models.IntegerField(default=0)),
                ('respawn', models.IntegerField(default=0)),
                ('disco', models.IntegerField(default=0)),
                ('ak_total', models.IntegerField(db_index=True, default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(db_index=True, default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('killboard_pvp', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('killboard_pve', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('status', models.CharField(choices=[('alive', 'alive'), ('killed', 'killed'), ('dead', 'dead'), ('captured', 'captured')], db_index=True, default='alive', max_length=12)),
                ('ce', models.FloatField(default=0)),
                ('kl', models.FloatField(default=0)),
                ('ks', models.FloatField(default=0)),
                ('khr', models.FloatField(default=0)),
                ('gkl', models.FloatField(default=0)),
                ('gks', models.FloatField(default=0)),
                ('gkhr', models.FloatField(default=0)),
                ('wl', models.FloatField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stats.Player')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stats.Profile')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stats.Tour')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'vlifes',
            },
        ),
        migrations.AlterField(
            model_name='award',
            name='type',
            field=models.CharField(choices=[('tour', 'tour'), ('mission', 'mission'), ('sortie', 'sortie'), ('vlife', 'vlife')], default='tour', max_length=8, verbose_name='type'),
        ),
        migrations.AddField(
            model_name='sortie',
            name='vlife',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sorties_list', to='stats.VLife'),
        ),
    ]
