# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WP7Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(blank=True, db_index=True, max_length=20, verbose_name='BC01 barcode number')),
                ('object_id', models.PositiveIntegerField()),
                ('box_number', models.CharField(blank=True, max_length=20, null=True)),
                ('position_in_box', models.CharField(blank=True, max_length=3, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='bloodsample',
            name='barcode',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='BC01 barcode number'),
        ),
        migrations.AlterField(
            model_name='perfusatesample',
            name='barcode',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='BC01 barcode number'),
        ),
        migrations.AlterField(
            model_name='tissuesample',
            name='barcode',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='BC01 barcode number'),
        ),
        migrations.AlterField(
            model_name='urinesample',
            name='barcode',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='BC01 barcode number'),
        ),
    ]
