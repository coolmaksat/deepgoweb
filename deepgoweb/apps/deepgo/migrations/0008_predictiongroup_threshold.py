# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0007_protein'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictiongroup',
            name='threshold',
            field=models.FloatField(default=0.3),
        ),
    ]
