# Generated by Django 2.2.4 on 2019-09-02 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deepgo', '0017_auto_20190902_1205'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together={('protein', 'go_id')},
        ),
    ]
