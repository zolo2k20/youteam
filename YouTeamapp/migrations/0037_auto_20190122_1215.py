# Generated by Django 2.1.5 on 2019-01-22 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0036_auto_20190122_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 22, 12, 15, 27, 813247)),
        ),
    ]
