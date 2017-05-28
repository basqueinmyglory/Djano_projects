# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=500)),
                ('currency', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('impact', models.CharField(max_length=50)),
                ('time_eastern', models.CharField(max_length=50)),
                ('forecast', models.CharField(max_length=50)),
                ('previous', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='dailyforecast',
            old_name='pub_date',
            new_name='entry_date',
        ),
        migrations.AlterField(
            model_name='dailyforecast',
            name='notes',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='dailyforecast',
            name='strong_reason',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='dailyforecast',
            name='weak_reason',
            field=models.TextField(max_length=500),
        ),
    ]