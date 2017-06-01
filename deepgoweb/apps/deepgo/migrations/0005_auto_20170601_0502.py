# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0004_auto_20160705_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='protein_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='predictiongroup',
            name='data_format',
            field=models.CharField(choices=[('enter', 'Raw Sequence'), ('fasta', 'FASTA')], default='enter', max_length=10),
        ),
    ]
