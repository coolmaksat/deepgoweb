# Generated by Django 2.2.4 on 2019-09-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0016_auto_20190902_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='gene',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
