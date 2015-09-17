#!/usr/bin/python
# coding: utf-8
from django.contrib import admin
from django.utils import timezone

from .models import Sample


class SampleAdmin(admin.ModelAdmin):
    exclude = ('created_on', 'created_by')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.created_on = timezone.now()
        obj.save()

admin.site.register(Sample, SampleAdmin)