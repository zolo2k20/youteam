# Generated by Django 2.1.5 on 2019-01-30 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0043_auto_20190130_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freeall',
            old_name='pid',
            new_name='user_pid',
        ),
        migrations.AlterField(
            model_name='devoloperprofile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 30, 9, 25, 49, 526012)),
        ),
    ]
