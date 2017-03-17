# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import livefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_locked', models.BooleanField(default=False, help_text='locked by the admin team')),
                ('live', livefield.fields.LiveField(default=True)),
                ('description', models.CharField(max_length=50, verbose_name='AC01 category description')),
            ],
            options={
                'verbose_name': 'AECm1 adverse event category',
                'verbose_name_plural': 'AECm2 adverse event categories',
                'permissions': (('view_event', 'Can only view the data'),),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_locked', models.BooleanField(default=False, help_text='locked by the admin team')),
                ('live', livefield.fields.LiveField(default=True)),
                ('serious_eligible_1', models.BooleanField(default=False, verbose_name='AE10 lead to death')),
                ('serious_eligible_2', models.BooleanField(default=False, verbose_name='AE11 life threatening illness')),
                ('serious_eligible_3', models.BooleanField(default=False, verbose_name='AE12 permanent impairment')),
                ('serious_eligible_4', models.BooleanField(default=False, verbose_name='AE13 hospitalisation')),
                ('serious_eligible_5', models.BooleanField(default=False, verbose_name='AE14 prolonged hospitalisation')),
                ('serious_eligible_6', models.BooleanField(default=False, verbose_name='AE15 surgery required')),
                ('onset_at_date', models.DateField(verbose_name='AE02 onset date')),
                ('event_ongoing', models.BooleanField(default=True, verbose_name='AE03 event ongoing')),
                ('description', models.TextField(blank=True, null=True, verbose_name='AE06 description')),
                ('action', models.TextField(blank=True, null=True, verbose_name='AE07 action')),
                ('outcome', models.TextField(blank=True, null=True, verbose_name='AE08 outcome')),
                ('alive_query_1', models.BooleanField(default=False, verbose_name='AE20 incapcity')),
                ('alive_query_2', models.BooleanField(default=False, verbose_name='AE21 usual activity')),
                ('alive_query_3', models.BooleanField(default=False, verbose_name='AE22 no sequelae')),
                ('alive_query_4', models.BooleanField(default=False, verbose_name='AE23 device deficiency')),
                ('alive_query_5', models.BooleanField(default=False, verbose_name='AE24 device user error')),
                ('alive_query_6', models.BooleanField(default=False, verbose_name='AE25 life threatening illness')),
                ('alive_query_7', models.BooleanField(default=False, verbose_name='AE26 permanent impairment')),
                ('alive_query_8', models.BooleanField(default=False, verbose_name='AE27 prolonged hospitalisation')),
                ('alive_query_9', models.BooleanField(default=False, verbose_name='AE28 surgery required')),
                ('rehospitalisation', models.BooleanField(default=False, verbose_name='AE30 rehospitalisation')),
                ('date_of_admission', models.DateField(blank=True, null=True, verbose_name='AE31 date of admission')),
                ('date_of_discharge', models.DateField(blank=True, null=True, verbose_name='AE32 date of discharge')),
                ('admitted_to_itu', models.BooleanField(default=False, verbose_name='AE33 admitted to ITU')),
                ('dialysis_needed', models.BooleanField(default=False, verbose_name='AE34 dialysis needed')),
                ('biopsy_taken', models.BooleanField(default=False, verbose_name='AE35 biopsy taken')),
                ('surgery_required', models.BooleanField(default=False, verbose_name='AE36 surgery required')),
                ('rehospitalisation_comments', models.TextField(blank=True, null=True, verbose_name='AE37 comments')),
                ('death', models.BooleanField(default=False, verbose_name='AE40 led to death')),
                ('treatment_related', models.PositiveSmallIntegerField(blank=True, choices=[(2, 'MMc03 Unknown'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], null=True, verbose_name='AE49 treatment related?')),
                ('cause_of_death_1', models.BooleanField(default=False, verbose_name='AE42 cerebrovascular')),
                ('cause_of_death_2', models.BooleanField(default=False, verbose_name='AE43 multi organ')),
                ('cause_of_death_3', models.BooleanField(default=False, verbose_name='AE44 pneumonia')),
                ('cause_of_death_4', models.BooleanField(default=False, verbose_name='AE45 sepsis')),
                ('cause_of_death_5', models.BooleanField(default=False, verbose_name='AE46 transplant related')),
                ('cause_of_death_6', models.BooleanField(default=False, verbose_name='AE47 other')),
                ('cause_of_death_comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='AE48 comments')),
                ('categories', models.ManyToManyField(to='adverse_event.Category')),
            ],
            options={
                'verbose_name': 'AEm1 adverse event',
                'verbose_name_plural': 'AEm2 adverse events',
                'permissions': (('view_event', 'Can only view the data'), ('restrict_to_national', 'Can only use data from the same location country'), ('restrict_to_local', 'Can only use data from a specific location')),
            },
        ),
    ]
