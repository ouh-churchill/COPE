#!/usr/bin/python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from braces.views import LoginRequiredMixin, OrderableListMixin

from wp4.theme.layout import AjaxReturnIDMixin
from .models import QualityOfLife
from .forms import QualityOfLifeForm


@permission_required('health_economics.add_qualityoflife')
@login_required
def index(request):
    return render(request, 'health_economics/index.html', {})


class AjaxFormMixin(object):
    form_class = QualityOfLifeForm

    def form_valid(self, form):
        if self.request.is_ajax():
            self.object = form.save()
            return self.render_to_response(self.get_context_data(form=form))
        else:
            return super(AjaxFormMixin, self).form_valid(form)

    def form_invalid(self, form):
        print("DEBUG: form_invalid() errors: %s" % form.errors)
        error_count = len(form.errors)
        error_pluralise = "" if error_count == 1 else "s"
        messages.error(
            self.request,
            '<strong>Form was NOT saved</strong>, please correct the %d error%s below' %
            (error_count, error_pluralise)
        )
        return super(AjaxFormMixin, self).form_invalid(form)

    def get_form(self, form_class=None):
        form = super(AjaxFormMixin, self).get_form(form_class)
        # Both post() and get() call get_form() first, so this is best place to intercept ajax changes
        if self.request.is_ajax():
            self.template_name = "health_economics/qualityoflife_form.ajax.html"
            form.fields['recipient'].widget = forms.HiddenInput()
        return form


# ============================================  CBVs
class QualityOfLifeListView(AjaxReturnIDMixin, LoginRequiredMixin, OrderableListMixin, ListView):
    model = QualityOfLife
    ordering = "id"
    paginate_by = 100
    paginate_orphans = 5
    orderable_columns = ("id", "recipient__organ__trial_id", "date_recorded")
    orderable_columns_default = "recipient__organ__trial_id"


class QualityOfLifeBaselineListView(QualityOfLifeListView):
    queryset = QualityOfLife.objects.filter(followup_3m__isnull=True, followup_1y__isnull=True)
    template_name = "health_economics/qualityoflife_baseline_list.html"


class QualityOfLifeMonth3ListView(QualityOfLifeListView):
    queryset = QualityOfLife.objects.filter(followup_3m__isnull=False, followup_1y__isnull=True)
    template_name = "health_economics/qualityoflife_month3_list.html"


class QualityOfLifeFinalListView(QualityOfLifeListView):
    queryset = QualityOfLife.objects.filter(followup_3m__isnull=True, followup_1y__isnull=False)
    template_name = "health_economics/qualityoflife_final_list.html"


class QualityOfLifeDetailView(AjaxReturnIDMixin, DetailView):
    model = QualityOfLife


class QualityOfLifeCreateView(AjaxReturnIDMixin, AjaxFormMixin, LoginRequiredMixin, CreateView):
    model = QualityOfLife


class QualityOfLifeUpdateView(AjaxReturnIDMixin, AjaxFormMixin, LoginRequiredMixin, UpdateView):
    model = QualityOfLife
