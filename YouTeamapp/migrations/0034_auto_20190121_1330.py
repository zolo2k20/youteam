# Generated by Django 2.1.5 on 2019-01-21 13:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('YouTeamapp', '0033_auto_20190121_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expirence',
            fields=[
                ('programing_language', models.CharField(max_length=100)),
                ('user_tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('expirencepl', models.IntegerField(default=0, null=True)),
                ('framework', models.CharField(max_length=200)),
                ('expirencefw', models.IntegerField(default=0, null=True)),
                ('frontend_technology', models.CharField(max_length=200)),
                ('expirenceft', models.IntegerField(default=0, null=True)),
                ('data_base', models.CharField(max_length=200)),
                ('expirencedb', models.IntegerField(default=0, null=True)),
                ('other_skills', models.CharField(max_length=200)),
                ('expirenceos', models.IntegerField(default=0, null=True)),
                ('development_tools', models.CharField(max_length=200, null=True)),
                ('operating_system', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='technology',
            name='user_tech',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 21, 13, 30, 8, 398663)),
        ),
        migrations.DeleteModel(
            name='technology',
        ),
    ]
