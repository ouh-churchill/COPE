# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followups', '0002_followup1y_followup3m_followup6m_followupinitial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup1y',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB10 graft failure'),
        ),
        migrations.AddField(
            model_name='followup1y',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB14 graft removal'),
        ),
        migrations.AddField(
            model_name='followup3m',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB10 graft failure'),
        ),
        migrations.AddField(
            model_name='followup3m',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB14 graft removal'),
        ),
        migrations.AddField(
            model_name='followup6m',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB10 graft failure'),
        ),
        migrations.AddField(
            model_name='followup6m',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB14 graft removal'),
        ),
        migrations.AddField(
            model_name='followupinitial',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB10 graft failure'),
        ),
        migrations.AddField(
            model_name='followupinitial',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB14 graft removal'),
        ),
    ]