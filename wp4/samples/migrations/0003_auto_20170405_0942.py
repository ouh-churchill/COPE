# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20170405_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wp7record',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='wp7record',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
