# Generated by Django 2.1.7 on 2020-11-16 10:00

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0022_auto_20201116_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictiongroup',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False),
        ),

    ]
