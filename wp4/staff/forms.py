#!/usr/bin/python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

import re

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes

from .models import Person


class PersonForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.html5_required = True
    helper.layout = Layout(
        'first_name',
        'last_name',
        'based_at',
        'telephone',
        'email',
        InlineCheckboxes('groups'),
    )

    def __init__(self, data=None, *args, **kwargs):
        # Special intercept and clean of data to account for jQuery.serialise data mangling of lists
        # TODO: Check that this is needed or working... jobs having been superseded by Groups
        if data is not None:
            jquery_serialise_list_pattern = re.compile("^\[(\d+,?\s?)+\]$")
            if isinstance(data['jobs'], type(u'')) and jquery_serialise_list_pattern.match(data['jobs']):
                data = data.copy()  # make it mutable
                data['jobs'] = [int(i) for i in data['jobs'][1:-1].split(",")]
        super(PersonForm, self).__init__(data=data, *args, **kwargs)
        self.render_required_fields = True

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'telephone', 'email', 'based_at', 'groups')