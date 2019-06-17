# Generated by Django 2.1.5 on 2019-01-24 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0039_auto_20190124_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='devloperprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pic', models.FileField(null=True, upload_to='images/')),
                ('Datetime', models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 24, 11, 58, 45, 498894))),
                ('Designation', models.CharField(max_length=100)),
                ('complete_project', models.CharField(max_length=100)),
                ('salary_year', models.FloatField()),
                ('salary_month', models.FloatField(null=True)),
                ('salary_hour', models.FloatField(null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('State', models.CharField(max_length=100, null=True)),
                ('Zip_code', models.CharField(max_length=10, null=True)),
                ('offical_email', models.CharField(max_length=80, null=True)),
                ('LinkedIn_profile_url', models.CharField(max_length=100, null=True)),
                ('cover', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 24, 11, 58, 45, 498513)),
        ),
    ]