# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 20:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('followups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup6m',
            name='rejection_periods',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='F606 rejection periods'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='calcineurin',
            field=models.NullBooleanField(verbose_name='FB19 calcineurin inhibitor'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='creatinine_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FY02 creatinine clearance'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='currently_on_dialysis',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'MMc03 Unknown'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], null=True, verbose_name='FY03 currently on dialysis'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='dialysis_requirement_1',
            field=models.DateField(blank=True, null=True, verbose_name='FB10 date of dialysis requirement 1'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='dialysis_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc10 CAPD'), (2, 'FBc11 Hemodialysis'), (3, 'FBc12 Unknown')], null=True, verbose_name='FB11 Dialysis type'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_complications',
            field=models.TextField(blank=True, verbose_name='FY06 graft function complications'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB02 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_failure_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB05 date of graft failure'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_failure_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc01 Immunological'), (2, 'FBc02 Preservation'), (3, 'FBc03 Technical - artery'), (4, 'FBc04 Technical - venous'), (5, 'FBc05 Infection - bacterial'), (6, 'FBc06 Infection - viral'), (10, 'FBc07 Other')], null=True, verbose_name='FB03 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_failure_type_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB04 Other failure type'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB06 graft removal'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='graft_removal_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB07 date of graft removal'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='immunosuppression',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc20 Azathioprine'), (2, 'FBc21 Cyclosporin'), (3, 'FBc22 MMF'), (4, 'FBc23 Prednisolone'), (5, 'FBc24 Sirolomus'), (6, 'FBc25 Tacrolimus'), (7, 'FBc26 Other')], null=True, verbose_name='FB12 Post tx immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='immunosuppression_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB13 Other immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='notes',
            field=models.TextField(blank=True, verbose_name='FB20 general notes'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='number_of_dialysis_sessions',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='FY04 number of dialysis sessions'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='qol_anxiety',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='FY14 qol anxiety or depression score'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='qol_mobility',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='FY10 qol mobility score'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='qol_pain',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='FY13 qol pain or discomfort score'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='qol_selfcare',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='FY11 qol self care score'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='qol_usual_activities',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='FY12 qol usual activites score'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection',
            field=models.NullBooleanField(verbose_name='FB14 rejection'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection_biopsy',
            field=models.NullBooleanField(verbose_name='FB18 biopsy proven'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection_drug',
            field=models.NullBooleanField(verbose_name='FB16 treated with other drug'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection_drug_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB17 Other rejection drug'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection_periods',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='FY05 rejection periods'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='rejection_prednisolone',
            field=models.NullBooleanField(verbose_name='FB15 treated with prednisolone'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='serum_creatinine_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FB08 creatinine 1'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='FB01 start date'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='urine_creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FY01 urine creatinine'),
        ),
        migrations.AlterField(
            model_name='followup1y',
            name='vas_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='FY15 vas score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='calcineurin',
            field=models.NullBooleanField(verbose_name='FB19 calcineurin inhibitor'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='creatinine_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='F302 creatinine clearance'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='currently_on_dialysis',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'MMc03 Unknown'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], null=True, verbose_name='F303 currently on dialysis'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='dialysis_requirement_1',
            field=models.DateField(blank=True, null=True, verbose_name='FB10 date of dialysis requirement 1'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='dialysis_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc10 CAPD'), (2, 'FBc11 Hemodialysis'), (3, 'FBc12 Unknown')], null=True, verbose_name='FB11 Dialysis type'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_complications',
            field=models.TextField(blank=True, verbose_name='F306 graft function complications'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB02 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_failure_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB05 date of graft failure'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_failure_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc01 Immunological'), (2, 'FBc02 Preservation'), (3, 'FBc03 Technical - artery'), (4, 'FBc04 Technical - venous'), (5, 'FBc05 Infection - bacterial'), (6, 'FBc06 Infection - viral'), (10, 'FBc07 Other')], null=True, verbose_name='FB03 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_failure_type_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB04 Other failure type'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB06 graft removal'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='graft_removal_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB07 date of graft removal'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='immunosuppression',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc20 Azathioprine'), (2, 'FBc21 Cyclosporin'), (3, 'FBc22 MMF'), (4, 'FBc23 Prednisolone'), (5, 'FBc24 Sirolomus'), (6, 'FBc25 Tacrolimus'), (7, 'FBc26 Other')], null=True, verbose_name='FB12 Post tx immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='immunosuppression_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB13 Other immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='notes',
            field=models.TextField(blank=True, verbose_name='FB20 general notes'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='number_of_dialysis_sessions',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='F304 number of dialysis sessions'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='qol_anxiety',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='F311 qol anxiety or depression score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='qol_mobility',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='F307 qol mobility score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='qol_pain',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='F310 qol pain or discomfort score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='qol_selfcare',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='F308 qol self care score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='qol_usual_activities',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='F309 qol usual activites score'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection',
            field=models.NullBooleanField(verbose_name='FB14 rejection'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection_biopsy',
            field=models.NullBooleanField(verbose_name='FB18 biopsy proven'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection_drug',
            field=models.NullBooleanField(verbose_name='FB16 treated with other drug'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection_drug_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB17 Other rejection drug'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection_periods',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='F305 rejection periods'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='rejection_prednisolone',
            field=models.NullBooleanField(verbose_name='FB15 treated with prednisolone'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='serum_creatinine_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FB08 creatinine 1'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='FB01 start date'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='urine_creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='F301 urine creatinine'),
        ),
        migrations.AlterField(
            model_name='followup3m',
            name='vas_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='F312 vas score'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='calcineurin',
            field=models.NullBooleanField(verbose_name='FB19 calcineurin inhibitor'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='creatinine_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='F602 creatinine clearance'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='currently_on_dialysis',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'MMc03 Unknown'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], null=True, verbose_name='F603 currently on dialysis'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='dialysis_requirement_1',
            field=models.DateField(blank=True, null=True, verbose_name='FB10 date of dialysis requirement 1'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='dialysis_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc10 CAPD'), (2, 'FBc11 Hemodialysis'), (3, 'FBc12 Unknown')], null=True, verbose_name='FB11 Dialysis type'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_complications',
            field=models.TextField(blank=True, verbose_name='F605 graft function complications'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB02 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_failure_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB05 date of graft failure'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_failure_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc01 Immunological'), (2, 'FBc02 Preservation'), (3, 'FBc03 Technical - artery'), (4, 'FBc04 Technical - venous'), (5, 'FBc05 Infection - bacterial'), (6, 'FBc06 Infection - viral'), (10, 'FBc07 Other')], null=True, verbose_name='FB03 graft failure'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_failure_type_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB04 Other failure type'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB06 graft removal'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='graft_removal_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB07 date of graft removal'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='immunosuppression',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc20 Azathioprine'), (2, 'FBc21 Cyclosporin'), (3, 'FBc22 MMF'), (4, 'FBc23 Prednisolone'), (5, 'FBc24 Sirolomus'), (6, 'FBc25 Tacrolimus'), (7, 'FBc26 Other')], null=True, verbose_name='FB12 Post tx immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='immunosuppression_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB13 Other immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='notes',
            field=models.TextField(blank=True, verbose_name='FB20 general notes'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='number_of_dialysis_sessions',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='F604 number of dialysis sessions'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='rejection',
            field=models.NullBooleanField(verbose_name='FB14 rejection'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='rejection_biopsy',
            field=models.NullBooleanField(verbose_name='FB18 biopsy proven'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='rejection_drug',
            field=models.NullBooleanField(verbose_name='FB16 treated with other drug'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='rejection_drug_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB17 Other rejection drug'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='rejection_prednisolone',
            field=models.NullBooleanField(verbose_name='FB15 treated with prednisolone'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='serum_creatinine_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FB08 creatinine 1'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='FB01 start date'),
        ),
        migrations.AlterField(
            model_name='followup6m',
            name='urine_creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='F601 urine creatinine'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='calcineurin',
            field=models.NullBooleanField(verbose_name='FB19 calcineurin inhibitor'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_cause',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FIc01 Delayed graft function'), (2, 'FIc02 Hyperkalemia'), (3, 'FIc03 Fluid overload'), (4, 'FIc04 Other')], null=True, verbose_name='FI20 Dialysis cause'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_cause_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FI21 Other dialysis cause'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_1',
            field=models.DateField(blank=True, null=True, verbose_name='FB10 date of dialysis requirement 1'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_2',
            field=models.DateField(blank=True, null=True, verbose_name='FI10 date of dialysis requirement 2'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_3',
            field=models.DateField(blank=True, null=True, verbose_name='FI11 date of dialysis requirement 3'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_4',
            field=models.DateField(blank=True, null=True, verbose_name='FI12 date of dialysis requirement 4'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_5',
            field=models.DateField(blank=True, null=True, verbose_name='FI13 date of dialysis requirement 5'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_6',
            field=models.DateField(blank=True, null=True, verbose_name='FI14 date of dialysis requirement 6'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_requirement_7',
            field=models.DateField(blank=True, null=True, verbose_name='FI15 date of dialysis requirement 7'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='dialysis_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc10 CAPD'), (2, 'FBc11 Hemodialysis'), (3, 'FBc12 Unknown')], null=True, verbose_name='FB11 Dialysis type'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='discharge_date',
            field=models.DateField(blank=True, null=True, verbose_name='FI26 date of primary post tx discharge'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_failure',
            field=models.NullBooleanField(verbose_name='FB02 graft failure'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_failure_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB05 date of graft failure'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_failure_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc01 Immunological'), (2, 'FBc02 Preservation'), (3, 'FBc03 Technical - artery'), (4, 'FBc04 Technical - venous'), (5, 'FBc05 Infection - bacterial'), (6, 'FBc06 Infection - viral'), (10, 'FBc07 Other')], null=True, verbose_name='FB03 graft failure'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_failure_type_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB04 Other failure type'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_removal',
            field=models.NullBooleanField(verbose_name='FB06 graft removal'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='graft_removal_date',
            field=models.DateField(blank=True, null=True, verbose_name='FB07 date of graft removal'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='hla_mismatch_a',
            field=models.CharField(blank=True, max_length=10, verbose_name='FI22 HLA A'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='hla_mismatch_b',
            field=models.CharField(blank=True, max_length=10, verbose_name='FI23 HLA B'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='hla_mismatch_dr',
            field=models.CharField(blank=True, max_length=10, verbose_name='FI24 HLA DR'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='immunosuppression',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FBc20 Azathioprine'), (2, 'FBc21 Cyclosporin'), (3, 'FBc22 MMF'), (4, 'FBc23 Prednisolone'), (5, 'FBc24 Sirolomus'), (6, 'FBc25 Tacrolimus'), (7, 'FBc26 Other')], null=True, verbose_name='FB12 Post tx immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='immunosuppression_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB13 Other immunosuppression'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='induction_therapy',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'FIc10 IL 2'), (2, 'FIc11 ATG')], null=True, verbose_name='FI25 Induction therapy'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='notes',
            field=models.TextField(blank=True, verbose_name='FB20 general notes'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='rejection',
            field=models.NullBooleanField(verbose_name='FB14 rejection'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='rejection_biopsy',
            field=models.NullBooleanField(verbose_name='FB18 biopsy proven'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='rejection_drug',
            field=models.NullBooleanField(verbose_name='FB16 treated with other drug'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='rejection_drug_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='FB17 Other rejection drug'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='rejection_prednisolone',
            field=models.NullBooleanField(verbose_name='FB15 treated with prednisolone'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FB08 creatinine 1'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI01 creatinine 2'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI02 creatinine 3'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI03 creatinine 4'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI04 creatinine 5'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_6',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI05 creatinine 6'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='serum_creatinine_7',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='FI06 creatinine 7'),
        ),
        migrations.AlterField(
            model_name='followupinitial',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='FB01 start date'),
        ),
    ]
