# Generated by Django 2.1.7 on 2019-04-15 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0010_auto_20171001_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='predictions', to='deepgo.PredictionGroup'),
        ),
        migrations.AlterField(
            model_name='predictiongroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prediction_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
