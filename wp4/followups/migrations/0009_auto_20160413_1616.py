# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_economics', '0001_initial'),
        ('followups', '0008_auto_20160413_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup1y',
            name='quality_of_life',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='health_economics.QualityOfLife', verbose_name='FY07 quality of life'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='followup3m',
            name='quality_of_life',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='health_economics.QualityOfLife', verbose_name='F307 quality of life'),
            preserve_default=False,
        ),
    ]