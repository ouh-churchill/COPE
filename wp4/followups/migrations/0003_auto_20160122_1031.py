# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followups', '0002_auto_20160121_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followupinitial',
            options={'verbose_name': 'FIm1 Initial FollowUp', 'verbose_name_plural': 'FIm2 Initial FollowUps'},
        ),
        migrations.AddField(
            model_name='followup1y',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='FB21 form completed'),
        ),
        migrations.AddField(
            model_name='followup3m',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='FB21 form completed'),
        ),
        migrations.AddField(
            model_name='followup6m',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='FB21 form completed'),
        ),
        migrations.AddField(
            model_name='followupinitial',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='FB21 form completed'),
        ),
    ]
