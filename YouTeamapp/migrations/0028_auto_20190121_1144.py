# Generated by Django 2.1.5 on 2019-01-21 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0027_auto_20190121_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 21, 11, 44, 10, 593774)),
        ),
        migrations.AlterField(
            model_name='technology',
            name='expirencedb',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='expirenceft',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='expirencefw',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='expirenceos',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='expirencepl',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
