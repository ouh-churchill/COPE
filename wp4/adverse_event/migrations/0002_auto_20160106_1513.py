# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverse_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adverseevent',
            options={'verbose_name': 'AEm1 adverse event', 'verbose_name_plural': 'AEm2 adverse events'},
        ),
    ]
